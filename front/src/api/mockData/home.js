export default {
    //getHomeData对外暴露一个方法，返回的是数据,本地mock的使用来模拟数据
    getHomeData:() =>{
        return {
            code:200,
            data:{
                tableData:[
                    {
                        date: '2023-05-03',
                        name: '吴先生',
                        address: '北京大运村2公寓0123',
                        tag: '肉类',
                        state: 'California',
                        city: 'San Francisco',
                        zip: 'CA 94114',
                        family: [
                            {
                                name: 'Jerry',
                                state: 'California',
                                city: 'San Francisco',
                                address: '北京大运村2公寓0123',
                                zip: 'CA 94114',
                            },
                            {
                                name: 'Spike',
                                state: 'California',
                                city: 'San Francisco',
                                address: '3650 21st St, San Francisco',
                                zip: 'CA 94114',
                            },
                            {
                                name: 'Tyke',
                                state: 'California',
                                city: 'San Francisco',
                                address: '3650 21st St, San Francisco',
                                zip: 'CA 94114',
                            },
                        ],
                    },
                    {
                        date: '2023-05-02',
                        name: '吴先生',
                        address: '北京大运村2公寓0123',
                        tag: '肉类',
                        state: 'California',
                        city: 'San Francisco',
                        zip: 'CA 94114',
                        family: [
                            {
                                name: 'Jerry',
                                state: 'California',
                                city: 'San Francisco',
                                address: '北京大运村2公寓0123',
                                zip: 'CA 94114',
                            },
                            {
                                name: 'Spike',
                                state: 'California',
                                city: 'San Francisco',
                                address: '3650 21st St, San Francisco',
                                zip: 'CA 94114',
                            },
                            {
                                name: 'Tyke',
                                state: 'California',
                                city: 'San Francisco',
                                address: '北京大运村2公寓0123',
                                zip: 'CA 94114',
                            },
                        ],
                    },
                    {
                        date: '2023-05-04',
                        name: '吴先生',
                        address: '北京大运村2公寓0123',
                        tag: '肉类',
                        state: '北京',
                        city: '海淀区',
                        zip: 'CA 94114',
                        family: [
                            {
                                name: 'Jerry',
                                state: '北京市1号仓库 to 京南转运中心',
                                city: '2023-5-4 8:12',
                                address: '2023-5-4 9:12',
                                zip: '已送达',
                            },
                            {
                                name: 'Mike',
                                state: '京南转运中心 to 海淀区生鲜转运中心',
                                city: '2023-5-4 9:32',
                                address: '2023-5-4 10:32',
                                zip: '已送达',
                            },
                            {
                                name: 'John',
                                state: '海淀区生鲜转运中心 to 北航生鲜超市',
                                city: '2023-5-4 10:42',
                                address: 'None',
                                zip: '运送中',
                            },
                        ],
                    },
                    {
                        date: '2023-05-01',
                        name: '吴先生',
                        address: '北京大运村2公寓0123',
                        tag: '蔬菜',
                        state: 'California',
                        city: 'San Francisco',
                        zip: 'CA 94114',
                        family: [
                            {
                                name: 'Jerry',
                                state: 'California',
                                city: 'San Francisco',
                                address: '3650 21st St, San Francisco',
                                zip: 'CA 94114',
                            },
                            {
                                name: 'Spike',
                                state: 'California',
                                city: 'San Francisco',
                                address: '3650 21st St, San Francisco',
                                zip: 'CA 94114',
                            },
                            {
                                name: 'Tyke',
                                state: 'California',
                                city: 'San Francisco',
                                address: '3650 21st St, San Francisco',
                                zip: 'CA 94114',
                            },
                        ]
                    },
                ]
            }
        }
    }
}