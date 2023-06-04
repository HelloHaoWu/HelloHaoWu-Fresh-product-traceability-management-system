import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import router from "./router/index.js"
import 'element-plus/dist/index.css'
import App from './App.vue'

// import echarts from 'echarts';
//以下为使用el-plus中的icons图标部分
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import './api/mock.js'
import { createPinia } from "pinia";
// import { IonicVueRouter } from '@ionic/vue';

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

// router.use(IonicVueRouter);

app.use(createPinia())
app.use(ElementPlus)
app.use(router)
app.mount('#app')
// app.use(echarts)



