<template>
    <!-- :gutter="20"为间隔 -->
    <el-row class="home" :gutter="20">
        <!-- style="margin-top: 20px"为上下间隔 -->
        <el-col :span="8" style="margin-top: 20px">

            <!-- 展示用户和登录信息 -->
            <!-- shadow="hover"为阴影 -->
            <el-card shadow="hover">
                <!-- 展示user信息 -->
                <div class="user">
                    <img :src="getImgSrc(username)" alt="" />
                    <div class="userinfo">
                        <p class="name" v-text='username'> </p>
                        <p class="role" v-text='getRole(username)'> </p>
                    </div>
                </div>
                <div class="login-info">
                    <!-- <p>
                        上次登录时间:<span>1990-01-01</span>
                    </p>
                    <p>
                        上次登录地点:<span>北京</span>
                    </p> -->
                </div>
            </el-card>
        
            <!-- 展示表格信息 -->
            <el-card shadow="hover" style="margin-top: 20px" height="450px">
                <el-table :data="tableData">
                    <el-table-column v-for="(val, key) in tableLabel"
                    :key="key" 
                    :prop="key"
                    :label="val"
                    >
                    </el-table-column>
                </el-table>
            </el-card>
        </el-col>
        <el-col :span="16" style="margin-top: 20px">
        </el-col>
    </el-row>
</template>

<script>
import { computed, defineComponent, getCurrentInstance, onMounted,ref } from 'vue';
import { useStore} from 'vuex';

// 异步调用
// import axios from 'axios';
export default defineComponent({
    setup() {
        // 动态引入图片
        let getImgSrc = (img)=>{
            // import.meta.url作为返回组件路径，作为基准
            // URL则是含有图片地址的对象
            // 打印 console.log(new URL(`../assets/images/${img}.jpg`, import.meta.url))
            return new URL(`../../assets/images/${img}.jpg`, import.meta.url).href;
        };
        // 判断角色
        let getRole = (username)=>{
            if (username == 'admin') {
                return '管理';
            } else if (username == 'haohao') {
                return '用户';
            } else if (username == 'deliver') {
                return '配送员';
            } else if (username == 'supplier') {
                return '供应商';
            }
            
        };

        // 表格数据
        let tableData = ref([]);
        // 表格标签
        const tableLabel={
            name:'课程',
            todayBuy:'今日购买',
            monthBuy:'本月购买',
            totalBuy:'总购买',
        };

        // 拿到全局api
        const {proxy} = getCurrentInstance();

        // 向后端请求数据（接口）
        const getTableList = async () => {
            /** 
             * 没封装的mock的写法
             * 
             * // 接收数据到变量res
             * // 本地mock写法，记得配置mock.js await axios.get("/home/getData").then((res) => {
             * await axios.get("https://www.fastmock.site/mock/94f906bf2a0251b1228cffab616e8254/api/home/getTableData").then((res) => {
             *     // 打印 console.log(res);
             *     // 先判断，再渲染数据
             *    if(res.data.code ==200){
             *         tableData.value = res.data.data;
             *     }
             * });
             **/
            
            // 需要掉接口就去api/api.js下加一个方法就行
            let res = await proxy.$api.getTableData();
            tableData.value = res;
        };
        onMounted(()=>{
            getTableList();
            });

        // 取得用户名字
        let store = useStore();
        const username = computed(()=>{
            return store.state.loginForm.username;
        });

        return {
            getImgSrc,
            getRole,
            tableData,
            tableLabel,
            username,
        };
    },
})
</script>


<style lang="less" scoped>
// 设置home样式
.home{
    // user信息样式
    .user{
        display: flex;
        align-items: center;
        padding-bottom: 20px;
        border-bottom: 1px solid #ccc;
        margin-bottom: 20px;
        img{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-right: 40px;
        }
        .userinfo{
            width: 100%;
            .role{
                margin-top: 10px;
            }
        }
    }
    // 登录信息样式
    .login-info{
        p{
            line-height: 30px;
            font-size: 14px;
            color: #999;
            text-align: left;
            margin-left: 10px;
            span{
                color: #666;
                margin-left: 60px;
            }
        }
    }
}
</style>