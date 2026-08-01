const platform = 'django'  //有三种模式:vue,django,cloud

const CONFIG_API = {
    HTTP_URL: '',
    VAD_URT: '',
}

if (platform === 'vue'){
    CONFIG_API.HTTP_URL = 'http://127.0.0.1:8000'
    CONFIG_API.VAD_URT = 'http://localhost:5173/vad/'
} else if(platform === 'django'){
    CONFIG_API.HTTP_URL = 'http://127.0.0.1:8000'
    CONFIG_API.VAD_URT = 'http://127.0.0.1:8000/static/frontend/vad/'
} else if(platform === 'cloud'){
    CONFIG_API.HTTP_URL = 'www.yuhentai.xyz'
    CONFIG_API.VAD_URT = 'www.yuhentai.xyz/static/frontend/vad/'
}

export default CONFIG_API
