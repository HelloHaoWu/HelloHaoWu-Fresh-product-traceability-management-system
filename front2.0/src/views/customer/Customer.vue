<template>
  <el-row>
    <el-col :span="24">
      <el-card class="customerCard">
        <!--        table组件内容-->
        <!--                    data就是table数据部分-->
        <el-button @click="resetDateFilter">reset date filter</el-button>
        <el-button @click="clearFilter">reset all filters</el-button>
        <el-table ref="tableRef" row-key="date" :data="tableData" stripe style="width: 100%">
          <!--            <div class="tableExpander">-->
          <el-table-column type ="expand" :data="tableData" class="tableExpander">
            <template #default="props">
              <div m="4">
                <p m="t-0 b-2">省份/直辖市: {{ props.row.state }}</p>
                <p m="t-0 b-2">城市/区: {{ props.row.city }}</p>
                <p m="t-0 b-2">收货地址: {{ props.row.address }}</p>
                <p m="t-0 b-2">订单编号: {{ props.row.zip }}</p>
                <h3>产品溯源系统跟踪信息：</h3>
                <el-card >
                  <el-table :data="props.row.family" :border="childBorder">
                    <el-table-column label="负责人" prop="name" />
                    <el-table-column label="发出地点-目标地点" prop="state" />
                    <el-table-column label="发出时间" prop="city" />
                    <el-table-column label="到达时间" prop="address" />
                    <el-table-column label="订单状态" prop="zip" />
                  </el-table>
                </el-card>
              </div>
            </template>
          </el-table-column>
          <!--            </div>-->
          <el-table-column
              prop="date"
              label="下单日期"
              sortable
              width="180"
              column-key="date"
              :filters="[
                            { text: '2023-05-01', value: '2023-05-01' },
                            { text: '2023-05-02', value: '2023-05-02' },
                            { text: '2023-05-03', value: '2023-05-03' },
                            { text: '2023-05-04', value: '2023-05-04' },
                          ]"
              :filter-method="filterHandler"
          />
          <el-table-column prop="name" label="姓名" width="180" />
          <el-table-column prop="address" label="地址" :formatter="formatter" />

          <el-table-column
              prop="tag"
              label="Tag"
              width="100"
              :filters="[
                  { text: '肉类', value: '肉类' },
                  { text: '蔬菜', value: '蔬菜' },
                ]"
              :filter-method="filterTag"
              filter-placement="bottom-end">
            <template #default="scope">
              <el-tag
                  :type="getTagColor(scope.row.tag)"
                  disable-transitions>
                {{ scope.row.tag }}
              </el-tag>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>
  </el-row>
</template>

<style>
.customerCard{
  color: #111111;
  height: 700px;
  /*margin-top: 70px;*/
  /*margin-right: 50px;*/
  margin-top: 70px;
  /*margin-right: 50px;*/
  margin-left: -80px;
  margin-right: 30px;
}

.customerTable{
  color: #1a1a1a;
  font-size: 1rem;
}

.tableHeader{
  color:#111111;
}

.tableExpander{
  width : 10px;
}

</style>

<script lang="ts">
import { ref ,onMounted,defineComponent} from 'vue'
import axios from "axios";//借用异步调用请求模块
export default defineComponent({
  data() {
    let tableData = ref([])

    //async即为axios中的模块之一，意为“异步”，其中的await函数可以实现功能
    const getTableList = async () => {
      址https://www.fastmock.site/mock/4adca991e257e0e3a89c8de7cad6295e/api
          // await axios.get('/home/getData').then((res)=>{
          //   // console.log(res.data.data.tableData);
          //   tableData.value = res.data.data.tableData
          // })
          await axios.get('https://www.fastmock.site/mock/4adca991e257e0e3a89c8de7cad6295e/api/home/getData').then((res)=>{
            // console.log(res.data.tableData);
            tableData.value = res.data.tableData

          })
    }
    onMounted(() => {
      getTableList()
    });

    return {
      tableData,
    }
  },
  methods: {
    getTagColor(tag) {
      switch (tag) {
        case '肉类':
          return 'danger'; // red
        case '蔬菜':
          return 'success'; // green
        default:
          return 'info'; // blue (or any other color you want to use as the default)
      }
    },
    // ...
  }
})
</script>


<script lang="ts" setup>
import { ref ,onMounted,defineComponent} from 'vue'
import type { TableColumnCtx, TableInstance } from 'element-plus'


const parentBorder = ref(false)
const childBorder = ref(false)

interface User {
  date: string//下单时间
  name: string//客户姓名
  address: string//收货地址
  tag: string//产品类型（暂定）
  state: string//客户性别
  city: string//客户联系方式
  // address: string//客户联系方式
  zip: string//订单明细编号
  family:object//订单详细信息，一个列表，包含供应商编号
// {
//   "name": "Jerry",//供应商名称
//     "state": "California",//供应商编号
//     "city": "San Francisco",//配送人员编号
//     "address": "北京大运村2公寓0123",//配送人员联系方式
//     "zip": "CA 94114"//仓库编号
// },
}

const tableRef = ref<TableInstance>()

const resetDateFilter = () => {
  tableRef.value!.clearFilter(['date'])
}
// TODO: improvement typing when refactor table
const clearFilter = () => {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-expect-error
  tableRef.value!.clearFilter()
}
const formatter = (row: User, column: TableColumnCtx<User>) => {
  return row.address
}
const filterTag = (value: string, row: User) => {
  return row.tag === value
}
const filterHandler = (
    value: string,
    row: User,
    column: TableColumnCtx<User>
) => {
  const property = column['property']
  return row[property] === value
}

</script>