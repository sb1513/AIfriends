import { createRouter, createWebHistory } from 'vue-router'
import HomePageIndex from "@/views/homepage/HomePageIndex.vue";
import FrinedsIndex from "@/views/friends/FrinedsIndex.vue";
import CreatesIndex from "@/views/creates/CreatesIndex.vue";
import NotFoundIndex from "@/views/errors/NotFoundIndex.vue";
import LoginIndex from "@/views/user/accounts/LoginIndex.vue";
import RegisterIndex from "@/views/user/accounts/RegisterIndex.vue";
import SpaceIndex from "@/views/user/space/SpaceIndex.vue";
import ProfileIndex from "@/views/user/profile/ProfileIndex.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomePageIndex,
      name: 'homepage-index',
    },
    {
      path: '/friend/',
      component: FrinedsIndex,
      name: 'friends-index',
    },
    {
      path: '/create/',
      component: CreatesIndex,
      name: 'creates-index',
    },
    {
      path: '/404/',
      component: NotFoundIndex,
      name: '404',
    },
    {
      path: '/user/accounts/login/',
      component: LoginIndex,
      name: 'user-accounts-login-index',
    },
    {
      path: '/user/accounts/register/',
      component: RegisterIndex,
      name: 'user-accounts-register-index',
    },
    {
      path: '/user/space/:user_id/',
      component: SpaceIndex,
      name: 'user-space-index',
    },
    {
      path: '/user/profile/',
      component: ProfileIndex,
      name: 'user-profile-index',
    },
    {
      path: '/:pathMatch(.*)*',
      component: NotFoundIndex,
      name: 'not-found'
    },
  ],
})

export default router
