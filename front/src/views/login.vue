<template>
  <el-form :model="loginFrom" class="login-container">
    <h3>系统登录</h3>
    <el-form-item>
      <!-- v-model="loginForm.username"双向绑定 -->
      <el-input type="input" placeholder="请输入账号" v-model="username">
      </el-input>
    </el-form-item>

    <el-form-item>
      <el-input type="password" placeholder="请输入密码" v-model="password">
      </el-input>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="login"> 登录 </el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { defineStore } from 'pinia';
export const useUserStore = defineStore('userid', {
  state: () => {
    return {
      user: ''
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

<style lang="less" scoped>
.login-container {
  width: 350px;
  background-color: #fff;
  border: 1px solid #eaeaea;
  border-radius: 15px;
  padding: 35px 35px 15px 35px;
  box-shadow: 0 0 25px #cacaca;
  margin: 250px auto;
  h3{
    text-align: center;
    margin-bottom: 20px;
    color: #505450;
  }
  :deep(.el-form-item__content) {
    justify-content: center;
  }

}
</style>