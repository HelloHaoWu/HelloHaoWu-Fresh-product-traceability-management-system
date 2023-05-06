<template>
  <el-row>
    <el-col :span="10">
      <el-card class="box-card">
        <div class = card1>
          <div class = userPhoto>
            <img src = "../assets/xiaobao.png" alt="">
          </div>
          <div class = userInfo>
            <z class="name">Administer<br></z>
            <z class="access">超级管理员<br></z>
          </div>
        </div>
        <!--        以下为分界线元素-->
        <el-divider></el-divider>

        <div class = logInInfo>
          <z>上次登录时间:<span class="span1">2023-4-5<br></span></z>
          <z>上次登陆地点:<span class="span1">北京</span></z>
        </div>
      </el-card>
    </el-col>
    <!--    第一行伪元素填充-->
    <el-col :span="24">
      <div>
        <null class="br-Any"></null>
      </div>
    </el-col>
    <el-col :span="10">
      <el-card class="box-card2">
        <div class="card2-Content">关于我们:<br><br>
          一家专注于生鲜产品（水果、鲜奶、肉类等等）的线上销售企业，已经有一个完整的线上销售平台<br>
          our 人:供应商（上游）、客户（下游）、配送人员、客服人员...<br>
          our 事:仓储管理、销售管理、配送管理...<br>
          our 物:产品、车辆、仓库

        </div>
      </el-card>
    </el-col>

  </el-row>



</template>

<script>
export default {
  name: "AppHome",
  data() {
    return {}
  }
}
</script>

<style>
.card1{
  display: flex;
  /*display设定格式布局，flex是对容器进行的约束。但是其实作用与容器内部的元素，并使这个容器成为弹性容器*/
  align-items: center;/*垂直居中*/
  /*直接字母是在指定自定义标签（这一步貌似可以再后半句之中设定class内部的标签css样式），点加单词是描述对应的class*/
}
img{
  /*图像高和宽*/
  width:150px;
  height:150px;
  /*图像变成圆形边框*/
  border-radius: 50%;
  /*向右偏移的距离，像素为单位*/
  margin-right: 40px;
}
.userInfo{

}
.access{
  color:#999999;
}
.name{
  /*字体大小*/
  font-size: 32px;
  /*向下边距*/
  margin-bottom: 10px;
}
.box-card{
  margin-left: -90px;
}

.logInInfo{
  color:#666666;
}

.span1{
  margin_left:60px;
}
.box-card2{
  margin-left:-90px;
  margin-right:0px;
  margin-top: 10px;
  height: 288px;
  /*margin-top: 400px;*/
}
.card2-Content{
  font-size: 16px;
}

</style>
