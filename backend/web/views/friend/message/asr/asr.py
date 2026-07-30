import asyncio
import json
import os
import uuid

import websockets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ASRView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        audio = request.FILES.get('audio')
        if not audio:
            return Response({
                'result': '音频不存在'
            })
        pcm_data = audio.read()
        text = asyncio.run(self.run_asr_task(pcm_data))
        return Response({
            'result': 'success',
            'text': text,
        })


    async def asr_sender(self, pcm_data, ws, task_id):
        chunk = 6400
        for i in range(0, len(pcm_data), chunk):
            await ws.send(pcm_data[i: i + chunk])
            await asyncio.sleep(0.01)
        await ws.send(json.dumps({
            "header": {
                "action": "finish-task",
                "task_id": task_id,
                "streaming": "duplex"
            },
            "payload": {
                "input": {}
            }
        }))

    async def asr_receiver(self, ws):
        text = ''
        async for msg in ws:
            data = json.loads(msg)
            event = data['header']['event']
            if event == 'result-generated':
                output = data['payload']['output']
                if output.get('sentence', None) and output['sentence']['sentence_end']:
                    text += output['sentence']['text']
            elif event in ['task-finished', 'task-failed']:
                break
        return text


    async def run_asr_task(self, pcm_data):
        task_id = uuid.uuid4().hex
        api_key = os.getenv('API_KEY')
        wss_asr_url = os.getenv('WSS_ASR_URL')
        headers = {
            'Authorization': f"Bearer {api_key}"
        }
        async with websockets.connect(wss_asr_url, additional_headers=headers) as ws:
            await ws.send(json.dumps({
                "header": {
                "action": "run-task",
                "task_id": task_id,
                "streaming": "duplex"
                },
                "payload": {
                    "task_group": "audio",
                    "task": "asr",
                    "function": "recognition",
                    "model": "paraformer-realtime-v2",
                    "parameters": {
                        "format": "pcm",
                        "sample_rate": 16000,
                        "disfluency_removal_enabled": False,
                        "language_hints": [
                            
                        ],
                        "semantic_punctuation_enabled": True,
                    },
                    "input": {}
                }
            }))
            async for msg in ws:
                if json.loads(msg)['header']['event'] == 'task-started':
                    break
            _, text = await asyncio.gather(
                self.asr_sender(pcm_data, ws, task_id),
                self.asr_receiver(ws),
            )
            return text