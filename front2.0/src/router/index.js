import { createRouter, createWebHashHistory } from "vue-router"

const routes = [
    {
        path: '/',
        component: () => import('../views/Main.vue'),
        name: 'home1',
        // 重定向，默认进入后跳转home
        redirect: '/login',
        // 静态路由
        /**
         *  children: [
         *   {
         *       path: '/',
         *       name: 'home',
         *       component:() => import('../views/home/Home.vue'),
         *   },
         *   {
         *       path: '/user',
         *       name: 'user',
         *       component:() => import('../views/user/User.vue'),
         *   }
         * ]
         **/
        // 动态路由
        children: []
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/Login.vue'),
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router