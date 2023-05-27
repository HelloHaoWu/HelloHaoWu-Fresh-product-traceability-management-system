<script setup>
// 一下动态路由应该写在main.js里，否则不能动态路由
// import { useStore } from "vuex";
// import { useRouter } from "vue-router";
    
//     const store = useStore();

//     const router = useRouter();
//     // 调用addMenu，使得左侧菜单数据持久化（面试可能会问）
//     store.commit("addMenu", router);
</script>

<template>
    <router-view />
</template>


<style >
/* 大的页面布局 注意max-width: 100% */
    #app{
        height: 100%;
        width: 100%;
        margin: 0px;
        padding: 0px;
        border:0px;
        max-width: 100%;
        max-height: 100%;
    }
    html,body{
        height: 100%;
        width: 100%;
        margin: 0px;
        padding: 0px;
        border:0px;
    }
</style>