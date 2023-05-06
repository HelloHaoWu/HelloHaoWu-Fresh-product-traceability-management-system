import{ createRouter,createWebHashHistory} from "vue-router";

const routes = [
        //主路由
        {
            path:'/',
            component:()=> import("../components/SelfAside.vue"),
            children:[
                //子路由（嵌套路由）
                { path: '/home',name:'home', component:()=> import("../views/Home.vue"), },//主页
                { path: '/customer',name:'customer', component:()=> import("../views/Customer-test.vue"), },//客户
                { path: '/manager',name:'manager',component:()=> import("../views/Manager.vue")},//管理
                { path: '/manage-1',name:'manage-1', component:()=> import("../views/manage-1.vue"), },//管理分界面1
                { path: '/manage-2',name:'manage-2', component:()=> import("../views/manage-2.vue"), },//管理分界面2
                { path: '/manage-3',name:'manage-3', component:()=> import("../views/manage-3.vue"), },//管理分界面3
                { path: '/supplier', name:'supplier',component:()=> import("../views/Supplier.vue"), },//供应商
                { path: '/deliver', name:'deliver',component:()=> import("../views/Deliver.vue"), },//配送人员
                { path: '/settings',name:'settings', component:()=> import("../views/Settings.vue"), },//设置
            ],
        },
]
//这里是为了创建一个路由，才能导出
const router = createRouter({
    history:createWebHashHistory(),//create开头的基本都是方法，是方法引入了就要调用
    routes
})

export default router