<template>
<!--  <head>-->
<!--    <meta charset="UTF-8">-->
<!--    <meta name="viewport" content="width=device-width, initial-scale=1.0">-->

<!--    &lt;!&ndash; ===== 引入 ===== &ndash;&gt;-->
<!--    <link rel="stylesheet" href="assets/css/styles.css">-->

<!--    <title>侧边栏子菜单</title>-->
<!--  </head>-->
  <body id="body-pd">
    <div class = my-header>
<!--header部分-->
      你好，管理员

    </div>
    <div class="l-navbar" id="navbar">
      <nav class="nav">
        <div>
          <div class="nav__brand">
<!--            <router-link to = "/">-->
<!--            注意使用el-icon会使得其中不能添加class标签随意修改格式，必须使用el官网的标签信息来进行调整格式-->
            <div class = "nav__toggle" >
              <el-icon id="nav-toggle" @click="showMenu('nav-toggle','navbar','body-pd')"><Menu /></el-icon>
            </div>
              <a class="nav__logo">生鲜平台管理系统</a>
<!--              <a>内部文字是标题，href是默认跳转方式-->
<!--            </router-link>-->
          </div>
          <div class="nav__list">
            <router-link to="/home" class="nav__link active">
              <div class = "nav__icon">
                <el-icon ><House /></el-icon>
              </div>
                <span class="nav__name">主页</span>
            </router-link>
            <router-link to="/customer" v-if="show_customerpage()" class="nav__link">
              <div class = "nav__icon">
                <el-icon><User /></el-icon>
              </div>
              <span class="nav__name">客户</span>
            </router-link>


            <router-link to="/deliver" v-if="show_dispatcherpage()" class="nav__link">
              <div class = "nav__icon">
                <el-icon><Share /></el-icon>
              </div>
              <span class="nav__name">配送人员</span>
            </router-link>
<!--            <a href="#" class="nav__link">-->
              <router-link to="/supplier" v-if="show_supplierpage()" class="nav__link">
                <div class = "nav__icon">
                  <el-icon><Promotion /></el-icon>
                </div>
                <span class="nav__name">供应商</span>
              </router-link>

<!--            </a>-->

            <div  class="nav__link collapse">
<!--              <router-link to="/manager" class="nav__link">-->
              <div class = "nav__icon">
                <el-icon><Service /></el-icon>
              </div>
              <span class="nav__name">管理</span>
<!--              </router-link>-->


              <div class = "collapse__link" >
                <el-icon><ArrowDown /></el-icon>
              </div>

              <ul class="collapse__menu">
                <router-link to = "/manage-1" class="manageDetails">
                  <a href="#" class="collapse__sublink">统计面板<br></a>
                </router-link>
                <router-link to = "/manage-2" class="manageDetails">
                  <a href="#" class="collapse__sublink">订单详览<br></a>
                </router-link>
                <router-link to = "/manage-3" class="manageDetails">
                  <a href="#" class="collapse__sublink">库存总览<br></a>
                </router-link>

              </ul>
            </div>

<!--            <a href="#" class="nav__link">-->
<!--              <router-link to="/user3" class="nav__link">-->
<!--                <ion-icon name="pie-chart-outline" class="nav__icon"></ion-icon>-->
<!--                <span class="nav__name">统计</span>-->
<!--              </router-link>-->

<!--            </a>-->


<!--            <div class="nav__link collapse">-->

<!--&lt;!&ndash;              <router-link to="/team" class="nav__link">&ndash;&gt;-->
<!--              <div class = "nav__icon">-->
<!--                <el-icon><Share /></el-icon>-->
<!--              </div>-->
<!--                <span class="nav__name">团队</span>-->
<!--&lt;!&ndash;              </router-link>&ndash;&gt;-->

<!--              <div class = "collapse__link">-->
<!--                <el-icon><ArrowDown /></el-icon>-->
<!--              </div>-->

<!--              <ul class="collapse__menu">-->
<!--                <a href="#" class="collapse__sublink">aaaa<br></a>-->
<!--                <a href="#" class="collapse__sublink">bbbb<br></a>-->
<!--                <a href="#" class="collapse__sublink">cccc<br></a>-->
<!--              </ul>-->
<!--            </div>-->
<!--            <a href="#" class="nav__link">-->


            <router-link to="settings" class="nav__link">
              <div class = "nav__icon">
                <el-icon><Tools /></el-icon>
              </div>
              <span class="nav__name">设置</span>
            </router-link>
<!--            </a>-->
          </div>
        </div>

        <a href="#" class="nav__link">
          <div class = "nav__icon">
            <el-icon><SwitchButton /></el-icon>
          </div>
          <span class="nav__name">退出登陆</span>
        </a>
      </nav>
    </div>

    <div class="right-side">
      <router-view></router-view>
    </div>

<!--    <h1>内容</h1>-->
<!--    &lt;!&ndash; ===== 引入icon ===== &ndash;&gt;-->
<!--&lt;!&ndash;    <script src="https://unpkg.com/ionicons@5.1.2/dist/ionicons.js"></script>&ndash;&gt;-->

<!--    &lt;!&ndash; ===== 引入js ===== &ndash;&gt;-->
<!--&lt;!&ndash;    <script src="assets/js/main.js"></script>&ndash;&gt;-->
<!--    </body>-->
<!--    </html>-->
<!--    <script src = "D:\大三下\信息系统分析与设计\test\my-app\src\js-outward\SelfAside_js.js"></script>-->
   </body>
</template>

<script>
/*===== EXPANDER MENU  =====*/
import {Menu} from "@element-plus/icons-vue";
import {useUserStore} from '../views/login.vue';
export default {
  name: 'SelfAside',
  components: {Menu},
  data() {
    const store = useUserStore();
    return {
      user: store.user
    }
  },
  mounted() {
    console.log(this.user)
    /*===== LINK ACTIVE  =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    function colorLink(){
      linkColor.forEach(l=> l.classList.remove('active'))
      this.classList.add('active')
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    /*===== COLLAPSE MENU  =====*/
    const linkCollapse = document.getElementsByClassName('collapse__link')
    var i

    for(i=0;i<linkCollapse.length;i++){
      linkCollapse[i].addEventListener('click', function(){
        const collapseMenu = this.nextElementSibling
        collapseMenu.classList.toggle('showCollapse')

        const rotate = collapseMenu.previousElementSibling
        rotate.classList.toggle('rotate')
      })
    }
  },
  methods: {
    showMenu(toggleId,navbarId,bodyId) {
      console.log('success to enter.')
      const toggle = document.getElementById(toggleId),
          navbar = document.getElementById(navbarId),
          bodypadding = document.getElementById(bodyId)
      if (toggle && navbar) {
        navbar.classList.toggle('expander')
        bodypadding.classList.toggle('body-pd')
      }
    },
    show_customerpage() {
      return this.user === 'customer' || this.user === 'manager';
    },
    show_dispatcherpage() {
      return this.user === 'dispatcher' || this.user === 'manager';
    },
    show_supplierpage() {
      return this.user === 'supplier' || this.user === 'manager';
    }
  }
}
</script>

<style>
/*===== 谷歌字体 =====*/
/*@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap");*/

/*===== css变量老师家哦 =====*/
:root{
  --nav-width: 92px;

  /*===== 自定义颜色 =====*/
  --first-color:  #0C5DF4;            /* #4169E1,#0C5DF4;*/
  --bg-color: #12192C;
  --bg-color:  #B0C4DE;        /*#4169E1;#B0C4DE;*/
  --sub-color: #B6CEFC;
  --white-color: #FFF;
  --grey-color: #333333;
  --black-color: #111111;

  /*===== 规定字体  =====*/
  --body-font: 'Poppins', sans-serif;
  --normal-font-size: 1rem;
  --small-font-size: .875rem;

  /*===== 设置z-index =====*/
  --z-fixed: 100;
}


/*===== 基础规定 =====*/
*,::before,::after{
  box-sizing: border-box;
}
body{
  position: relative;
  margin: 0;
  padding: 2rem 0 0 6.75rem;
  font-family: var(--body-font);
  font-size: var(--normal-font-size);
  transition: .5s;
}
h1{
  margin: 0;
}
ul{
  margin: 0;
  padding: 0;
  list-style: none;
}
a{
  text-decoration: none;
}

/*===== 左侧 nav =====*/
.l-navbar{
  position: fixed;
  top: 0;
  left: 0;
  width: var(--nav-width);
  height: 100vh;
  background-color: var(--grey-color);
  color: var(--white-color);
  padding: 1.5rem 1.5rem 2rem;
  transition: .5s;
  z-index: var(--z-fixed);
}

/*===== NAV =====*/
.nav{
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
}

.manageDetails{
  display: grid;
  grid-template-columns: max-content max-content;
  align-items: center;
  margin-left: -10px;
  column-gap: .75rem;
  padding: .75rem;
  color: var(--white-color);
  border-radius: .5rem;
  margin-bottom: 1rem;
  transition: .3s;
}

.nav__brand{
  font-size: 1rem;
  display: grid;
  grid-template-columns: max-content max-content;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}
.nav__toggle{
  font-size: 1.25rem;
  padding: .75rem;
  cursor: pointer;
}
.nav__logo{
  color: var(--white-color);
  font-weight: 600;
}

.nav__link{
  display: grid;
  grid-template-columns: max-content max-content;
  align-items: center;
  column-gap: .75rem;
  padding: .75rem;
  color: var(--white-color);
  border-radius: .5rem;
  margin-bottom: 1rem;
  transition: .3s;
  cursor: pointer;
}
.nav__link:hover{
  background-color: var(--first-color);
}
.nav__icon{
  font-size: 1.25rem;
}
.nav__name{
  font-size: var(--small-font-size);
}

/*菜单控件*/
.expander{
  width: calc(var(--nav-width) + 9.25rem);
}

/*给body增加边距*/
.body-pd{
  padding: 2rem 0 0 16rem;
}

/*选中的菜单状态*/
.active{
  background-color: var(--first-color);
}

.collapse{
  grid-template-columns: 20px max-content 1fr;
}
.collapse__link{
  justify-self: flex-end;
  transition: .5s;
}
.collapse__menu{
  display: none;
  padding: .75rem 2.25rem;
}
.collapse__sublink{
  color: var(--sub-color);
  font-size: var(--small-font-size);
}
.collapse__sublink:hover{
  color: var(--white-color);
}

.showCollapse{
  display: block;
}

.rotate{
  transform: rotate(180deg);
}

/*===== 上侧 header =====*/
.my-header{
  position: fixed;
  font-size: large;
  top: 0;
  left: 0vh;
  width: 212vh;
  height: 5vh;
  background-color: var(--grey-color);
  color: var(--white-color);
  padding: 1.5rem 20rem 2rem;
  transition: .5s;
  z-index: var(--z-fixed);
}

</style>
