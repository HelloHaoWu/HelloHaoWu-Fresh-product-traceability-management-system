import Mock from 'mockjs'
export default {
    // 根据用户名不同，展示不同菜单
  getMenu: config => {
    const { username, password } = JSON.parse(config.body)
    // 先判断用户是否存在
    // 判断账号和密码是否对应

    //账号演示:admin:客服人员（全部可以看）;haohao:客户;deliver:配送员;supplier:供应商;

    if (username === 'admin' && password === 'admin') {
      return {
        code: 200,
        data: {
          menu: [
            {
              path: '/home',
              name: 'home',
              label: '首页',
              icon: 'house',
              url: 'home/Home'
            },
            {
              path: '/customer',
              name: 'customer',
              label: '客户',
              icon: 'user',
              url: 'customer/customer'
            },
            {
              path: '/deliver',
              name: 'deliver',
              label: '配送人员',
              icon: 'Share',
              url: 'deliver/deliver'
            },
            {
              path: '/supplier',
              name: 'supplier',
              label: '供应商',
              icon: 'Promotion',
              url: 'supplier/supplier'
            },
            // {
            //   path: '/mall',
            //   name: 'mall',
            //   label: '商品管理',
            //   icon: 'video-play',
            //   url: 'mall/Mall'
            // },
            {
              label: '客服人员',
              icon: 'setting',
              children: [
                {
                  path: '/manager-1',
                  name: 'manager-1',
                  label: '页面1',
                  icon: 'location',
                  url: 'manager/Manager-1'
                },
                {
                  path: '/manager-2',
                  name: 'manager-2',
                  label: '页面2',
                  icon: 'location',
                  url: 'manager/Manager-2'
                },
                {
                  path: '/manager-3',
                  name: 'manager-3',
                  label: '页面3',
                  icon: 'location',
                  url: 'manager/Manager-3'
                }
              ]
            }
          ],
          token: Mock.Random.guid(),
          message: '获取成功'
        }
      }
    } else if (username === 'haohao' && password === 'haohao') {
      return {
        code: 200,
        data: {
          menu: [
            {
              path: '/',
              name: 'home',
              label: '首页',
              icon: 'house',
              url: 'home/Home'
            },
            {
              path: '/customer',
              name: 'customer',
              label: '客户',
              icon: 'user',
              url: 'customer/customer'
            }
          ],
          token: Mock.Random.guid(),
          message: '获取成功'
        }
      }
    } else if (username === 'deliver' && password === 'deliver') {
      return {
        code: 200,
        data: {
          menu: [
            {
              path: '/',
              name: 'home',
              label: '首页',
              icon: 'house',
              url: 'home/Home'
            },
            {
              path: '/deliver',
              name: 'deliver',
              label: '配送人员',
              icon: 'Share',
              url: 'deliver/deliver'
            }
          ],
          token: Mock.Random.guid(),
          message: '获取成功'
        }
      }
    } else if (username === 'supplier' && password === 'supplier') {
      return {
        code: 200,
        data: {
          menu: [
            {
              path: '/',
              name: 'home',
              label: '首页',
              icon: 'house',
              url: 'home/Home'
            },
            {
              path: '/supplier',
              name: 'supplier',
              label: '供应商',
              icon: 'Promotion',
              url: 'supplier/supplier'
            }
          ],
          token: Mock.Random.guid(),
          message: '获取成功'
        }
      }
    } else {
      return {
        code: -999,
        data: {
          message: '密码错误'
        }
      }
    }

  }
}