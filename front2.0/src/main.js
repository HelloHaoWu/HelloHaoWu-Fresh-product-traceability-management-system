import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

// 引入less（布局）
import './assets/less/index.less'

// 引入路由
import router from './router'

// 完整引入ElementPlus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// 引入icons
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

// 引入store（组件间互动）
import store from './store/index.js'

// 引入mock（后端数据模拟）
import './api/mock.js'

// 引入api
import api from './api/api.js'

const app = createApp(App)

// 将api挂载到全局
app.config.globalProperties.$api = api

// 动态路由
store.commit("addMenu", router);

// 使得loginForm持久化
store.commit("addName");

app.use(router).use(store)

app.use(ElementPlus)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }

app.mount('#app')
