<template>
  <div class="box">
    <div class="content">
      <div class="login-wrapper">
        <h1>登录</h1>
        <!-- ↓加.prevent点击时候不会刷新界面 -->
        <form @submit.prevent="login" class="login-form">
          <div class="username form-item">
            <span>使用邮箱或手机号</span>
            <input type="text" v-model="username" class="input-item">
          </div>
          <div class="password form-item">
            <span>密码</span>
            <input type="password" v-model="password" class="input-item">
          </div>
          <!--          <router-link to="/menu">-->
          <button class="login-btn">登录</button>
          <!--          </router-link>-->
        </form>
        <div class="divider">
          <span class="line"></span>
          <div class="divider-text">其他登录方式</div>
          <span class="line"></span>
        </div>
        <div class="other-login-wrapper">
          <div class="other-login-item">
            <img src="./images/QQ.png" alt="">
          </div>
          <div class="other-login-item">
            <img src="./images/WeChat.png" alt="">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineStore } from 'pinia';
export const useUserStore = defineStore('userid', {
  state: () => {
    return {
      user: '',
      isfresh: false
    }
  }
});
export default {
  name: "AppLogin",
  data() {
    return {
      username: "",
      password: ""
    }
  },
  // mounted() {
  //   if (!isfresh) {
  //     // 保证不再刷新
  //     this.isfresh = true;
  //     // 在页面挂载后刷新浏览器
  //     window.location.reload();
  //   }
  // },
  methods: {
    login() {
      if((this.username === "manager" || this.username === "customer" || this.username === "dispatcher" || this.username === "supplier") && this.password === "123456") {
        const store = useUserStore();
        store.user = this.username;
        this.$router.push("/home")
      }
      else {
        console.log(this.username)
        alert("用户名或密码错误")
      }
    }
  }
}
</script>

<style lang="less">
* {
  margin: 0;
  padding: 0;
}

/*公共CSS*/
.box {
  //margin-top: -2rem;
  margin-left: -3rem;
  //padding-right: 3rem;
  width: 100vw;
  height: 100vh;
  background-color: rgb(29, 67, 89);
}
.box .content .login-wrapper h1 {
  text-align: center;
}
.box .content .login-wrapper .login-form .form-item {
  margin: 20px 0;
}
.box .content .login-wrapper .login-form .form-item span {
  display: block;
  margin: 5px 20px;
  font-weight: 100;
}
.box .content .login-wrapper .login-form .form-item .input-item {
  width: 100%;
  border-radius: 40px;
  padding: 20px;
  box-sizing: border-box;
  font-size: 20px;
  font-weight: 200;
}
.box .content .login-wrapper .login-form .form-item .input-item:focus {
  outline: none;
}
.box .content .login-wrapper .login-form .login-btn {
  width: 100%;
  border-radius: 40px;
  color: #fff;
  border: 0;
  font-weight: 100;
  margin-top: 10px;
  cursor: pointer;
}
.box .content .login-wrapper .divider {
  width: 100%;
  margin: 20px 0;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}
.box .content .login-wrapper .divider span:nth-child(1) {
  flex: 1;
}
.box .content .login-wrapper .divider span:nth-child(3) {
  flex: 1;
}
.box .content .login-wrapper .divider .line {
  display: inline-block;
  max-width: 30%;
  width: 30%;
}
.box .content .login-wrapper .divider .divider-text {
  vertical-align: middle;
  margin: 0px 20px;
  line-height: 0px;
  display: inline-block;
  width: 100px;
}
.box .content .login-wrapper .other-login-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.box .content .login-wrapper .other-login-item {
  border: 1px solid rgb(214, 222, 228);
  padding: 10px;
  margin: 10px;
  cursor: pointer;
}

/*一般大于手机的尺寸CSS*/
@media (min-width: 767px) {
  .box {
    background-color: rgb(29, 67, 89);
  }
  .box .content {
    width: 85vw;
    height: 90vh;
    background: url("./images/login_two.jpg") no-repeat;
    background-size: 90% 100%;
    position: absolute;
    right: 15%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 20px;
    background-color: #fff;
  }
  .box .content .login-wrapper {
    width: 25vw;
    position: absolute;
    right: 15%;
    top: 50%;
    transform: translateY(-50%);
  }
  .box .content .login-wrapper h1 {
    text-align: center;
    font-size: 45px;
    color: rgb(81, 100, 115);
    margin-bottom: 40px;
  }
  .box .content .login-wrapper .login-form {
    margin: 10px 0;
  }
  .box .content .login-wrapper .login-form .form-item span {
    color: rgb(81, 100, 115);
  }
  .box .content .login-wrapper .login-form .form-item .input-item {
    height: 60px;
    border: 1px solid rgb(214, 222, 228);
  }
  .box .content .login-wrapper .login-form .login-btn {
    height: 50px;
    background-color: rgb(59, 72, 89);
    font-size: 20px;
  }
  .box .content .login-wrapper .divider .line {
    border-bottom: 1px solid rgb(214, 222, 228);
  }
  .box .content .login-wrapper .other-login-item {
    border-radius: 20px;
  }
  .box .content .login-wrapper .other-login-item img {
    width: 40px;
    height: 40px;
  }
}
/*手机端CSS*/
@media (max-width: 768px) {
  .box .content {
    width: 100vw;
    height: 100vh;
    background: url("./images/login_bg_phone.png") no-repeat;
    background-size: 100% 100%;
    display: flex;
    align-items: flex-start;
    justify-content: center;
  }
  .box .content .login-wrapper {
    width: 70%;
    height: 60%;
    padding-top: 15%;
  }
  .box .content .login-wrapper h1 {
    font-size: 30px;
    color: #fff;
  }
  .box .content .login-wrapper .login-form .form-item {
    margin: 10px 0;
  }
  .box .content .login-wrapper .login-form .form-item span {
    color: rgb(113, 129, 141);
  }
  .box .content .login-wrapper .login-form .form-item .input-item {
    height: 30px;
    border: 1px solid rgb(113, 129, 141);
    background-color: transparent;
    color: #fff;
  }
  .box .content .login-wrapper .login-form .login-btn {
    height: 40px;
    background-color: rgb(235, 95, 93);
    font-size: 16px;
  }
  .box .content .login-wrapper .divider .line {
    border-bottom: 1px solid #fff;
  }
  .box .content .login-wrapper .divider .divider-text {
    color: #fff;
  }
  .box .content .login-wrapper .other-login-item {
    border-radius: 15px;
  }
  .box .content .login-wrapper .other-login-item img {
    width: 35px;
    height: 35px;
  }
}/*# sourceMappingURL=style.css.map */
</style>