

<template>
<!-- Main布局：左侧边栏，头部，内容 -->
    <div class="common-layout">
        <!-- 调整布局高度，使得全屏 -->
      <el-container style="height:100%;" direction="vertival">
          <!-- 左侧边栏 -->
        <common-aside />
        <el-container class="r-container">
          <!-- 头部 -->
          <common-header />
          <!-- 内容 -->
          <el-main>
              <router-view />
          </el-main>
        </el-container>
      </el-container>
  </div>
</template>

<!-- 引入CommonHeader组件 -->
<script>
import {defineComponent} from 'vue'
import CommonHeader from '../components/CommonHeader.vue'
import CommonAside from '../components/CommonAside.vue'

export default defineComponent({
    components:{
        CommonHeader,
        CommonAside,
    },
});
</script>

<style lang="less" scoped>

.r-container{
  /* 使Main强制换行 */
  flex-wrap: wrap;
  & > .el-main{
    padding-top: 0px;
  };
}

/* 设置页面布局 */
.common-layout{
  height: 100%;
  & > .el-container{
    height: 100%;
      /* 使Main对齐header */
    align-items: baseline;
    padding: 0px;
    margin: 0px;

    & > .el-aside{
      height: 100%;
      background: #545c64;
      margin-top: 0px;

    };

  }
}
</style>