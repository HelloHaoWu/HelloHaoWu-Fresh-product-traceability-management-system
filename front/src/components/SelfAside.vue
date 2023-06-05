<template>
  <body id="body-pd">
    <div class="l-navbar" id="navbar">
      <nav class="nav">
        <div>
          <div class="nav_brand">
            <ion-icon name="menu-outline" class="nav_toggle" id="nav_toggle" @click="showMenu('nav_toggle', 'navbar', 'body-pd')"></ion-icon>
            <!-- ↑图标相关, name的"menu-outline"表示菜单图标(三个横) -->
            <a class="nav_logo">生鲜管理系统</a>
          </div>
          <div class="nav__list">
            <router-link to="/home" class="nav_link active">
              <ion-icon name="home-outline" class="nav_icon"></ion-icon>
              <!-- ↑图标相关, name的"manage-outline"表示小房子图表 -->
              <!-- ↑在index.html(一般在public中)中</body>上方添加<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>语句引入-->
              <span class="nav_name">主页</span>
            </router-link>
            <router-link to="/customer" v-if="show_customerpage()" class="nav_link">
              <ion-icon name="person-outline" class="nav_icon"></ion-icon>
              <span class="nav_name">客户</span>
            </router-link>
            <router-link to="/deliver" v-if="show_dispatcherpage()" class="nav_link">
              <ion-icon name="analytics-outline" class="nav_icon"></ion-icon>
              <span class="nav__name">配送</span>
            </router-link>
            <div class="nav_link collapse" v-if="show_managerpage()">
              <ion-icon name="layers-outline" class="nav_icon"></ion-icon>
              <span class="nav__name">管理</span>
              <ion-icon id="collapselink" name="chevron-down-outline" class="collapse__link"></ion-icon>
              <ul class="collapse_menu">
                <router-link to = "/manage-1" class="collapse__sublink">统计面板<br></router-link>
                <router-link to = "/manage-2" class="collapse__sublink">订单详览<br></router-link>
                <router-link to = "/manage-3" class="collapse__sublink">库存总览<br></router-link>
              </ul>
            </div>
            <router-link to="/settings" class="nav_link">
              <ion-icon name="settings-outline" class="nav_icon"></ion-icon>
              <span class="nav_name">设置</span>
            </router-link>
          </div>
        </div>
        <router-link to="/" class="nav_link">
          <ion-icon name="log-out-outline" class="nav_icon"></ion-icon>
          <span class="nav_name">退出登录</span>
        </router-link>
      </nav>
    </div>

    <div class="right-side">
      <router-view></router-view>
    </div>
  </body>
</template>

<script>
// import 'https://unpkg.com/browse/ionicons@5.1.2/icons/index.js';
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
    // 加载菜单
    showMenu(toggleId, navbarID, bodyId) {
      const toggle = document.getElementById(toggleId),
          navbar = document.getElementById(navbarID),
          bodypadding = document.getElementById(bodyId);
      if (toggle && navbar) {
        navbar.classList.toggle('expander')
        bodypadding.classList.toggle('body-pd')
        const linkCollapse = document.getElementById('collapselink')
        if (linkCollapse.nextElementSibling.classList.toggle('showCollapse') == true) {
          linkCollapse.nextElementSibling.classList.toggle('showCollapse')
        }
        if (linkCollapse.classList.toggle('rotate') == true) {
          linkCollapse.classList.toggle('rotate')
        }
        // this.Willrefresh.refresh_picture = true
        // console.log(this.Willrefresh.refresh_picture)
      }
    },
    show_customerpage() {
      return this.user === 'customer' || this.user === 'manager';
    },
    show_dispatcherpage() {
      return this.user === 'dispatcher' || this.user === 'manager';
    },
    show_managerpage() {
      return this.user === 'manager';
    }
  }
}
</script>

<style lang="less">
  /*===== 谷歌字体 =====*/
  @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap");

  :root{
    --nav-width: 92px;

    /* 自定义颜色 */
    --first-color: #0c5df4;
    --bg-color: #12192c;
    --sub-color: #b6cefc;
    --white-color: #fff;

    /* 规定一下字体 */
    --body-font: 'Poppins', sans-serif;
    --normal-font-size: 1rem;
    /* 最小字体大小↓ */
    --smal-font-size: 0.875rem;

    /* 设置一下z-index级别 */
    --z-fixed: 100;
  }

  *,::before,::after{
    box-sizing: border-box;
  }
  body {
    /*相对定位*/
    position: relative;
    margin: 0;
    // ↓这行改与菜单栏的距离
    padding: 0 0 0 2.9rem;
    font-family: var(--body-font);
    transition: 0.5s;
  }
  h1 {
    margin: 0;
  }
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  a {
    /*下划线消失*/
    text-decoration: none;
  }
  .l-navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: var(--nav-width);
    /*100%窗口高度*/
    height: 100vh;
    background-color: var(--bg-color);
    color: var(--white-color);
    padding: 1.5rem 1.5rem 2rem;
    transition: 0.5s;
    z-index: var(--z-fixed);
  }
  .nav {
    height: 100%;
    display: flex;
    /*↓列排列(竖着排)*/
    flex-direction: column;
    justify-content: space-between;
    /*溢出隐藏*/
    overflow: hidden;
  }
  .nav_brand{
    /*↓设置该元素为网格容器*/
    display: grid;
    grid-template-columns: max-content max-content;
    // ↓这里原justify-content值为space-between, 即两端对其; 这里现在为从左到右按序排列
    justify-content: flex-start;
    align-items: center;
    margin-bottom: 2rem;
  }
  .nav_toggle {
    font-size: 1.25rem;
    padding: 0.75rem;
    /*↓鼠标放上变小手*/
    cursor: pointer;
  }
  .nav_logo {
    color: var(--white-color);
    font-weight: 600;
  }
  .nav_link {
    display: grid;
    grid-template-columns: max-content max-content;
    align-items: center;
    column-gap: 0.75rem;
    padding: 0.75rem;
    color: var(--white-color);
    border-radius: .5rem;
    margin-bottom: 1rem;
    transition: .3s;
    cursor: pointer;
  }
  /*↓选中变颜色*/
  .nav_link:hover {
    background-color: var(--first-color);
  }
  .nav_icon {
    font-size: 1.25rem;
  }
  .nav_name {
    font-size: var(--smal-font-size);
  }
  .expander {
    /*↓calc代表计算一下*/
    width:calc(var(--nav-width) + 7.50rem);
  }
  .body-pd {
    padding: 0rem 0 0 10.5rem;
  }
  /*↓默认被选中是啥状态*/
  .active {
    background-color: var(--first-color);
  }
  .collapse {
    /*↓制作一个四格容器??*/
    grid-template-columns: 20px max-content 1fr;
  }
  .collapse__link {
    justify-self: flex-end;
    transition: .5s;
  }
  .collapse_menu {
    /*↓附属栏内容消失*/
    display: none;
    padding: .75rem 2.25rem;
  }
  .collapse__sublink {
    // ↓强制不换行, 直到遇到<br>才换行(这里不知道为啥我没加<br>也达到效果了)
    white-space : nowrap;
    color: var(--sub-color);
    font-size: var(--smal-font-size);
  }
  /*↓"hover"表示被选中状态的CSS处理*/
  .collapse__sublink:hover {
    color: var(--white-color);
  }
  .showCollapse {
    display: block;
  }
  .rotate {
    transform: rotate(180deg);
  }
//.right-side {
//  position: absolute; /* 将元素脱离文档流 */
//  top: 20px; /* 调整元素在垂直方向上的位置 */
//  left: 145px; /* 调整元素在水平方向上的位置 */
//  right: 0; /* 元素的右侧与父元素的右侧保持对齐 */
//  bottom: 0; /* 元素的底部与父元素的底部保持对齐 */
//}
//:root{
//  --nav-width: 92px;
//
//  /*===== 自定义颜色 =====*/
//  --first-color:  #0C5DF4;            /* #4169E1,#0C5DF4;*/
//  --bg-color: #12192C;
//  --bg-color:  #B0C4DE;        /*#4169E1;#B0C4DE;*/
//  --sub-color: #B6CEFC;
//  --white-color: #FFF;
//  --grey-color: #333333;
//  --black-color: #111111;
//
//  /*===== 规定字体  =====*/
//  --body-font: 'Poppins', sans-serif;
//  --normal-font-size: 1rem;
//  --small-font-size: .875rem;
//
//  /*===== 设置z-index =====*/
//  --z-fixed: 100;
//}
//
//
///*===== 基础规定 =====*/
//*,::before,::after{
//  box-sizing: border-box;
//}
//body{
//  position: relative;
//  margin: 0;
//  padding: 2rem 0 0 6.75rem;
//  font-family: var(--body-font);
//  font-size: var(--normal-font-size);
//  transition: .5s;
//}
//.left_more{
//  margin-left: 238px;
//}
//h1{
//  margin: 0;
//}
//ul{
//  margin: 0;
//  padding: 0;
//  list-style: none;
//}
//a{
//  text-decoration: none;
//}
//
///*===== 左侧 nav =====*/
//.l-navbar{
//  position: fixed;
//  top: 0;
//  left: 0;
//  width: var(--nav-width);
//  height: 100vh;
//  /*background-color: var(--grey-color);*/
//  color: var(--white-color);
//  background-color: #213547;
//  padding: 1.5rem 1.5rem 2rem;
//  transition: .5s;
//  z-index: var(--z-fixed);
//}
//
///*===== NAV =====*/
//.nav{
//  height: 100%;
//  display: flex;
//  flex-direction: column;
//  justify-content: space-between;
//  overflow: hidden;
//}
//
//.manageDetails{
//  display: grid;
//  grid-template-columns: max-content max-content;
//  align-items: center;
//  margin-left: -10px;
//  column-gap: .75rem;
//  padding: .75rem;
//  color: var(--white-color);
//  border-radius: .5rem;
//  margin-bottom: 1rem;
//  transition: .3s;
//}
//
//.nav__brand{
//  font-size: 1rem;
//  display: grid;
//  grid-template-columns: max-content max-content;
//  justify-content: space-between;
//  align-items: center;
//  margin-bottom: 2rem;
//}
//.nav__toggle{
//  font-size: 1.25rem;
//  padding: .75rem;
//  cursor: pointer;
//}
//.nav__logo{
//  color: var(--white-color);
//  font-weight: 600;
//}
//
//.nav__link{
//  display: grid;
//  grid-template-columns: max-content max-content;
//  align-items: center;
//  column-gap: .75rem;
//  padding: .75rem;
//  color: var(--white-color);
//  border-radius: .5rem;
//  margin-bottom: 1rem;
//  transition: .3s;
//  cursor: pointer;
//}
//.nav__link:hover{
//  background-color: var(--first-color);
//}
//.nav__icon{
//  font-size: 1.25rem;
//}
//.nav__name{
//  font-size: var(--small-font-size);
//}
//
///*菜单控件*/
//.expander{
//  width: calc(var(--nav-width) + 9.25rem);
//}
//
///*给body增加边距*/
//.body-pd{
//  padding: 2rem 0 0 16rem;
//}
//
///*选中的菜单状态*/
//.active{
//  background-color: var(--first-color);
//}
//
//.collapse{
//  grid-template-columns: 20px max-content 1fr;
//}
//.collapse__link{
//  justify-self: flex-end;
//  transition: .5s;
//}
//.collapse__menu{
//  display: none;
//  padding: .75rem 2.25rem;
//}
//.collapse__sublink{
//  color: var(--sub-color);
//  font-size: var(--small-font-size);
//}
//.collapse__sublink:hover{
//  color: var(--white-color);
//}
//
//.showCollapse{
//  display: block;
//}
//
//.rotate{
//  transform: rotate(180deg);
//}
//
///*===== 上侧 header =====*/
//.my-header{
//  position: fixed;
//  font-size: large;
//  top: 0;
//  left: 0vh;
//  width: 212vh;
//  height: 5vh;
//  /*background-color: var(--grey-color);*/
//  color: var(--white-color);
//  background-color:#112000;
//  padding: 1.5rem 20rem 2rem;
//  transition: .5s;
//  z-index: var(--z-fixed);
//  margin-left: 88px;/*238为展开后*/
//  align-items: center;
//  /*justify-content: center;*/
//  font-family: "Helvetica Neue", sans-serif;
//  font-size: 20px;
//  /*border-radius: 20px;*/
//  padding: 10px;
//
//}
</style>
