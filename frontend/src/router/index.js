import { createRouter, createWebHistory } from 'vue-router'
import HomePageIndex from "@/views/homepage/HomePageIndex.vue";
import FrinedsIndex from "@/views/friends/FrinedsIndex.vue";
import CreatesIndex from "@/views/creates/CreatesIndex.vue";
import NotFoundIndex from "@/views/errors/NotFoundIndex.vue";
import LoginIndex from "@/views/user/accounts/LoginIndex.vue";
import RegisterIndex from "@/views/user/accounts/RegisterIndex.vue";
import SpaceIndex from "@/views/user/space/SpaceIndex.vue";
import ProfileIndex from "@/views/user/profile/ProfileIndex.vue";
import {useUserStore} from "@/stores/user.js";
import UpdateCharcter from "@/views/creates/character/UpdateCharcter.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomePageIndex,
      name: 'homepage-index',
      meta:{
        needLogin: false,
      },
    },
    {
      path: '/friend/',
      component: FrinedsIndex,
      name: 'friends-index',
      meta:{
        needLogin: true,
      },
    },
    {
      path: '/create/',
      component: CreatesIndex,
      name: 'creates-index',
      meta:{
        needLogin: true,
      },
    },
    {
      path: '/create/character/update/:character_id/',
      component: UpdateCharcter,
      name: 'update-character',
      meta:{
        needLogin: true,
      },
    },
    {
      path: '/404/',
      component: NotFoundIndex,
      name: '404',
      meta:{
        needLogin: false,
      },
    },
    {
      path: '/user/accounts/login/',
      component: LoginIndex,
      name: 'user-accounts-login-index',
      meta:{
        needLogin: false,
      },
    },
    {
      path: '/user/accounts/register/',
      component: RegisterIndex,
      name: 'user-accounts-register-index',
      meta:{
        needLogin: false,
      },
    },
    {
      path: '/user/space/:user_id/',
      component: SpaceIndex,
      name: 'user-space-index',
      meta:{
        needLogin: true,
      },
    },
    {
      path: '/user/profile/',
      component: ProfileIndex,
      name: 'user-profile-index',
      meta:{
        needLogin: true,
      },
    },
    {
      path: '/:pathMatch(.*)*',
      component: NotFoundIndex,
      name: 'not-found',
      meta:{
        needLogin: false,
      },
    },
  ],
})

router.beforeEach((to,from)=>{
  const user = useUserStore()
  if(to.meta.needLogin && user.hasPulledUserInfo && !user.isLogin()){
    return {
      name: 'user-accounts-login-index'
    }
  }
  return true
})

export default router
