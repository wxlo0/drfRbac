import { createRouter, createWebHistory } from 'vue-router'
import {useStore} from "vuex";
import {message} from "ant-design-vue";
import store from "@/store";
const routes = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/pages/Login/index.vue'),
    },
    {
        path: '/',
        name: 'Layout',
        component: () => import('@/components/Layout/index.vue'),
        redirect: '/home',
        meta: { title: 'PC Admin' },
        children: [
            {
                path: '/home',
                name: 'Home',
                component: () => import('@/pages/Home/index.vue'),
                meta: { title: '后台首页' },
            },
            {
                path: '/user',
                name: 'User',
                component: () => import('@/pages/User/index.vue'),
                meta: { title: '用户管理' },
            },
            {
                path: '/student',
                name: 'Student',
                component: () => import('@/pages/Student/index.vue'),
                meta: { title: '学生管理' },
            },
            {
                path: '/role',
                name: 'Role',
                component: () => import('@/pages/Role/index.vue'),
                meta: { title: '角色管理' },
            },
            {
                path: '/permission',
                name: 'Permission',
                component: () => import('@/pages/Permission/index.vue'),
                meta: { title: '权限管理' },
            }
        ]
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: () => import(/* webpackChunkName: "not-found" */ '@/pages/404.vue')
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

const ignoreList = ['/login']
router.beforeEach((to, from, next) => {
    // 判断登录状态
    const token = store.getters.getToken;
    if (!token && to.path !== '/login') {
        message.warn("请先登录");
        next("/login"); // redirect to login page
    } else if(ignoreList.includes(to.path) || to.name === "NotFound"){
        next();
    } else {
        const tabs = store.getters.getTabs;
        let tabExist = tabs.some(tab => tab.key === to.path);
        if (!tabExist)
            store.commit('addTab',  { title: to.meta['title'], key: to.path });

        store.commit('changeActiveKey', to.path);
        next(); // if already logged in, just proceed
    }
});


export default router
