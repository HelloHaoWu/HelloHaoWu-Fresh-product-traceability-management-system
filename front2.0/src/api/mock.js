/**
 * 本地mock
 **/

import Mock from 'mockjs'
import homeApi from './mockData/home.js'
import permissionApi from './mockData/permission.js'

// 拦截请求
Mock.mock('/home/getData', homeApi.getHomeData)

// 获取本地permission的数据
Mock.mock(/permission\/getMenu/, 'post', permissionApi.getMenu)