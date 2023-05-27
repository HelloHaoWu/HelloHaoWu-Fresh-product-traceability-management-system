
<template>
    <el-header>
        <!-- 左边按钮里放Menu图标 -->
        <div class="l-content">  
            <el-button size="small">
                <el-icon :size="20">
                   <Menu />
                </el-icon>
            </el-button> 
            <!-- 面包屑 -->
            <el-breadcrumb separator="/" class="bread">
                <!-- 首页一定存在，所以直接写死 -->
                <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>

                <!-- 判断，显示点击的菜单-->
                <el-breadcrumb-item :to="current.path" v-if="current">{{ current.label }}</el-breadcrumb-item>
            </el-breadcrumb> 
        </div>
        <!-- 右边放图片+下拉菜单 -->
        <div class="r-content">
            <el-dropdown>
                <span class="el-dropdown-link">
                    <!-- 图片 -->
                <img class="user" :src="getImgSrc('1')" alt=""/>
                </span>
                <!-- 下拉菜单 -->
                <template #dropdown>
                    <el-dropdown-menu>
                        <el-dropdown-item>个人中心</el-dropdown-item>
                        <el-dropdown-item @click="handleLoginOut">退出</el-dropdown-item>
                    </el-dropdown-menu>
                </template>
            </el-dropdown>
        </div>
    </el-header> 
</template>

<script>
import { computed, defineComponent} from "vue-demi"
import { useRouter } from "vue-router";
import { useStore } from "vuex"


export default defineComponent ({
    setup() {
        // 动态引入图片
        let getImgSrc = (img)=>{
            // import.meta.url作为返回组件路径，作为基准
            // URL则是含有图片地址的对象
            // 打印 console.log(new URL(`../assets/images/${img}.jpg`, import.meta.url))
            return new URL(`../assets/images/${img}.jpg`, import.meta.url).href;
        };

        // 拿到面包屑需要的当前菜单变量，用到计算属性
        let store = useStore();
        const current = computed(()=>{
            return store.state.currentMenu;
        });

        const router = useRouter();

        // 退出并清除菜单，跳转到login
        const handleLoginOut = () => {
            store.commit('cleanMenu');
            router.push({
                name: 'login',
            });
        };

        return{
            getImgSrc,
            current,
            handleLoginOut,
        };
    },
});
</script>



<style lang="less" scoped>
// 设置header排版
header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    background: #333;
}
// 设置r-content中图片大小
.r-content{
    .user{
        width: 40px;
        height: 40px;
        border-radius: 50%;
    }
}
// 设置l-content中的样式
.l-content{
    display: flex;
    align-items: center;
    .el-button {
        margin-right: 20px;
    }
    h3{
        color: #fff;
    }
}
// /deep/为穿透 !important强制将样式应用于元素
// 设置面包屑颜色，指针样式
.bread  :deep(span){
    color: #fff !important;
    cursor: pointer !important;
}
</style>