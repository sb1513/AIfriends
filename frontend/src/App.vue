<script setup>

import SideBar from "@/components/sidebar/SideBar.vue";
import {onMounted} from "vue";
import {useUserStore} from "@/stores/user.js";
import api from "@/js/http/api.js";
import {useRoute, useRouter} from "vue-router";

const user = useUserStore()
const route = useRoute()
const router = useRouter()

onMounted(async ()=>{
  try{
    const res = await api.get('/api/user/accounts/get_user_info/')
    const data = res.data
    if (data.result === 'success'){
      user.setUserInfo(data)
    }
  }catch(err){
  }finally {
    user.setHasPulledUserInfo(true)

    if (route.meta.needLogin && !user.isLogin()){
      await router.replace({
        name: 'user-accounts-login-index'
      })
    }
  }
})
</script>

<template>
  <SideBar>
    <RouterView/>
  </SideBar>
</template>

<style scoped>

</style>
