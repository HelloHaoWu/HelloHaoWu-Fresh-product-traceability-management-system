/**
 * 整个项目api的管理
 **/

import request from "./request";
export default {
    // home组件 左侧表格数据获取
    getTableData(params) {
        return request({
            url: '/home/getTableData',
            method: 'get',
            data: params,
            mock: true
        })
    },

    // 根据用户的用户名不同，返回不一样的菜单列表（用本地mock）
    getMenu(params) {
        return request({
            url: '/permission/getMenu',
            method: 'post',
            data: params,
            mock: false
        })
    }
}