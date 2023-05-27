import axios from 'axios'
import config from '../config'
import { ElMessage } from 'element-plus'
const NETWORK_ERROR = '网络请求异常，请稍后测试'
// 创建一个axios实例对象
const service = axios.create({
    baseURL: config.baseApi
})

// 在请求之前的处理
service.interceptors.request.use((req) => {
    // 可以自定义header
    // jwt-token认证的时候
    return req
})

// 在请求之后的处理
service.interceptors.response.use((res) => {
    // 解构
    const { code, data, msg } = res.data
    // 根据后端协商情况定
    if (code == 200) {
        return data
    } else {
        // 网络请求错误
        ElMessage.error(msg || NETWORK_ERROR)
        return Promise.reject(msg || NETWORK_ERROR)
    }
})

// 封装的核心函数
function request(options) {
    // 数据格式
    // {
    //     method: 'get',
    //         data: { 
    //         },
    //     mock:false
    // }
    options.method = options.method || 'get'
    // 支持大小写
    if (options.method.toLowerCase() == 'get') {
        options.params = options.data
    }
    // 对mock的处理
    // 总mock
    let isMock = config.mock
    // 如果有需要，当总mock开关为关闭时，可以单个设置mock开启
    if (typeof options.mock !== 'undefined') {
        isMock = options.mock
    }
    // 对线上环境做处理
    // 如果是线上环境，就不能使用mock
    if (config.env == 'prod') {
        service.defaults.baseURL = config.baseApi
    } else {
        service.defaults.baseURL = isMock ? config.mockApi : config.baseApi
    }

    return service(options)
}

export default request