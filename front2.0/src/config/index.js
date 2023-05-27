/**
 * 环境配置文件
 * 一般包含三个环境
 * 开发环境
 * 测试环境
 * 线上环境
 **/

// 当前环境，默认为线上环境'prod'
const env = import.meta.env.MODE || 'prod'

const EnvConfig = {
    // 开发环境
    development: {
        baseApi: '/api',
        mockApi: 'https://www.fastmock.site/mock/94f906bf2a0251b1228cffab616e8254/api',
    },
    // 测试环境
    test: {
        baseApi: '//test.future.com/api',
        mockApi: 'https://www.fastmock.site/mock/94f906bf2a0251b1228cffab616e8254/api',
    },
    // 线上环境
    prod: {
        baseApi: '//future.com/api',
        mockApi: 'https://www.fastmock.site/mock/94f906bf2a0251b1228cffab616e8254/api',
    },
}

export default {
    env,
    // mock总开关
    mock: true,
    // 解构EnvConfig
    ...EnvConfig[env]
}