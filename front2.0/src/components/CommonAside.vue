<template>
    <el-aside width="200px">
        <!-- background-color 背景色 text-color 文字颜色 :collapse 是否折叠-->
        <el-menu class="el-menu-vertical-demo" background-color="#545c64" text-color="#ffffff" :collapse="false">
        <!-- 标题 -->
        <h3>后台管理</h3>
        <!-- 只有一级菜单 -->
        <!-- :index="item.path" v-for="item in noChildren()" :key="item.path" 判断和生成多级菜单 -->
        <!-- @click="clickMenu()" 点击、路由跳转-->
        <el-menu-item :index="item.path" v-for="item in noChildren()" :key="item.path"
         @click="clickMenu(item)"
        >
          <!-- 动态引入图标 -->
            <el-icon>
              <component class="icons" :is="item.icon" />
            </el-icon>
          <span>{{ item.label }}</span>
        </el-menu-item>

        <!-- 带二级菜单 -->
        <el-sub-menu :index="item.label" 
        v-for="item in hasChildren()" 
        :key="item.path">
            <!-- 一级菜单 -->
          <template #title>
            <el-icon>
              <component class="icons" :is="item.icon" />
            </el-icon>
            <span>{{ item.label }}</span>
          </template>
          <!-- 二级菜单 -->
          <el-menu-item-group >
              <!-- :index="subItem.path" v-for="(subItem,subIndex) in item.children" :key="subIndex" 判断和生成多级菜单 -->
              <!-- @click="clickMenu()" 点击、路由跳转-->
            <el-menu-item :index="subItem.path" v-for="(subItem,subIndex) in item.children" :key="subIndex"
             @click="clickMenu(subItem)"
            >
                <el-icon>
                    <component class="icons" :is="subItem.icon" />
                </el-icon>
                <span>{{ subItem.label }}</span>
            </el-menu-item>
          </el-menu-item-group>
          </el-sub-menu>
      </el-menu>

    </el-aside>
</template>

<style lang="less" scoped>
// 取消侧边栏边界
.el-menu{
  border-right: none;
  // 设置标题行高
  h3{
    line-height: 70px;
    text-align: center;
    color: #fff;
  }
}
</style>


<script>
import { useRouter } from 'vue-router';
import { useStore } from "vuex"
export default {
    setup() {
        const router = useRouter();

        const store = useStore();

        // 引入菜单数据
        // 动态菜单
        const asyncList = store.state.menu
        //   静态菜单
      //   const list = [
      //   {
      //     path: "/",
      //     name: "home",
      //     label: "首页",
      //     icon: "house",
      //     url: "Home/Home",
      //   },
      //   {
      //     path: "/mall",
      //     name: "mall",
      //     label: "商品管理",
      //     icon: "video-play",
      //     url: "MallManage/MallManage",
      //   },
      //   {
      //     path: "/user",
      //     name: "user",
      //     label: "用户管理",
      //     icon: "user",
      //     url: "UserManage/UserManage",
      //   },
      //   {
      //     label: "其他",
      //     icon: "location",
      //     path: "/other",
      //     children: [
      //       {
      //         path: "/page1",
      //         name: "page1",
      //         label: "页面1",
      //         icon: "setting",
      //         url: "Other/PageOne",
      //       },
      //       {
      //         path: "/page2",
      //         name: "page2",
      //         label: "页面2",
      //         icon: "setting",
      //         url: "Other/PageTwo",
      //       },
      //     ],
      //   },
      // ];
      // 判断是否有二级菜单
        
        const noChildren = ()=>{
            return asyncList.filter((item) => !item.children);
        };
        const hasChildren = ()=>{
            return asyncList.filter((item) => item.children);
        };
      // 路由跳转
        const clickMenu = (item) => {
          router.push({
            name:item.name,
          });
          
          // vuex管理面包屑
          store.commit('selectMenu', item)
        };

        return{
            noChildren,
            hasChildren,
            clickMenu,
        };
    },
};
</script>
