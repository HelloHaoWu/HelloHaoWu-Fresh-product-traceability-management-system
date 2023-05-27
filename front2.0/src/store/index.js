import { createStore } from 'vuex'
export default createStore({
    state: {
        currentMenu: null,
        menu: [],
        loginForm: null,
    },
    mutations: {
        selectMenu(state, val) {
            // 判断当前页面是否为home，若不是则赋值
            val.name == 'home' ? (state.currentMenu = null) : (state.currentMenu = val)
        },
        
        // 不同用户，不同菜单
        setMenu(state, val) {
            state.menu = val
            // 数据持久化，因为vuex刷新丢失
            localStorage.setItem('menu', JSON.stringify(val))
        },

        // 添加菜单
        addMenu(state, router) {
            // 如果获取不到值，直接return不管
            if (!localStorage.getItem('menu')) {
                return
            }
            // 从JSON中获取到了，则先转换，再赋值给state.menu
            const menu = JSON.parse(localStorage.getItem('menu'))
            state.menu = menu

            // 动态路由
            const menuArray = []

            menu.forEach(item => {
                // 如果有二级菜单，则获取并push children，否则直接push item
                if (item.children) {
                    item.children = item.children.map(item => {
                        let url = `../views/${item.url}.vue`
                        item.component = () => import(url)
                        return item
                    })
                    menuArray.push(...item.children)
                } else {
                    let url = `../views/${item.url}.vue`
                    item.component = () => import(url)
                    menuArray.push(item)
                }
            })
            // 将item添加到路由中
            menuArray.forEach(item => {
                router.addRoute('home1', item)
            })
        },

        // 清除菜单
        cleanMenu(state) {
            state.menu = []
            localStorage.removeItem('menu')
        },

        // 获取登录账号和密码
        getName(state, val) {
            state.loginForm = val
            // 数据持久化，因为vuex刷新丢失
            localStorage.setItem("loginForm", JSON.stringify(val))
        },

        // 添加登录账号和密码
        addName(state) {
            // 如果获取不到值，直接return不管
            if (!localStorage.getItem('loginForm')) {
                return
            }
            // 从JSON中获取到了，则先转换，再赋值给state.loginForm
            const loginForm = JSON.parse(localStorage.getItem('loginForm'))
            state.loginForm = loginForm
        },
    }
})
