<template>
  <el-row>
    <el-col :span="24">
      <el-card class="customerCard">
        <!--        table组件内容-->
        <!--                    data就是table数据部分-->
        <el-button @click="resetDateFilter">reset date filter</el-button>
        <el-button @click="clearFilter">reset all filters</el-button>
        <el-table ref="tableRef" row-key="date" :data="tableData" stripe style="width: 100%">
          <el-table-column type="expand" class="tableExpander" label = '全部展开' width="180">
            <template #default="props">
              <div class="table_expander_container">
                <el-card class="table_expander_card">
                  <p m="t-0 b-2">目标地址:{{ props.row.Order_Destination }}</p>
                  <p m="t-0 b-2">客户性别:{{ props.row.Customer_ID__Customer_Sex}}</p>
                  <p m="t-0 b-2">客户姓名:{{ props.row.Customer_ID__Customer_Name }}</p>
                  <h3>产品溯源系统跟踪信息：</h3><br>
                  <el-card class = 'inner_card'>
                    <el-table :data="props.row.family" :border="childBorder" :key = props.row.orderdetail__OrderDetail_ID>
                      <el-table-column label="订单明细编号" prop="orderdetail__OrderDetail_ID" />
                      <el-table-column label="供应商编号" prop="orderdetail__ProductBatch_ID__Supplier_ID" />
                      <el-table-column label="供应商名称" prop="orderdetail__ProductBatch_ID__Supplier_ID__Supplier_Name" />
                      <el-table-column label="配送员编号" prop="delivery__Dispatcher_ID" />
                    </el-table>
                  </el-card>
                </el-card>
              </div>
            </template>
          </el-table-column>

          <!--        </div>-->
          <el-table-column
              prop="Order_Time"
              label="下单日期"
              width="180"
              column-key="Order_Time"
              :filters="[
                            { text: '2023-05-23T17:23:00Z', value: '2023-05-23T17:23:00Z' },
                            { text: '2023-05-23T18:45:00Z', value: '2023-05-23T18:45:00Z' },
                            { text: '2023-05-23T19:12:00Z', value: '2023-05-23T19:12:00Z' },
                            { text: '2023-05-23T20:59:00Z', value: '2023-05-23T20:59:00Z' },
                          ]"
              :filter-method="filterHandler"
          />
          <el-table-column prop="Customer_ID__Customer_Name" label="客户姓名" width="180" />
          <el-table-column prop="Order_Destination" label="目标地址" :formatter="formatter" />

          <el-table-column
              prop="tag"
              label="Tag"
              width="100"
              :filters="[
                  { text: '肉类', value: '肉类' },
                  { text: '蔬菜', value: '蔬菜' },
                  { text: '奶类', value: '奶类' },
                  { text: '水果', value: '水果' },
                ]"
              :filter-method="filterTag"
              filter-placement="bottom-end">
            <template #default="scope">
              <el-tag
                  :type="getTagColor(scope.row.orderdetail__ProductBatch_ID__Product_ID__Product_Type)"
                  disable-transitions>
                {{ scope.row.orderdetail__ProductBatch_ID__Product_ID__Product_Type }}
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
  margin-top: 50px;
  margin-left: 80px;
  margin-right: 30px;
  max-height: 650px;
  overflow-y: scroll;
  margin-bottom: 10px !important;
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
.inner_card{
  height : 130px
}
</style>

<script lang="ts">
import { ref ,onMounted,defineComponent} from 'vue'
import axios from "axios";//借用异步调用请求模块
export default defineComponent({
  data() {
    let tableData = ref([])
    // const getTableList = async () => {
    //   await axios.get('http://43.143.167.222:8020/Customer/').then((res)=>{
    //     // console.log(this.row);
    //     tableData.value = res.data
    //   })
    // }
    const getTableList = async () => {
      await axios.get('http://43.143.167.222:8020/Customer/').then((res)=>{
        tableData.value = res.data.map((item) => {
          const newItem = { ...item }
          newItem.family = [
            {
              orderdetail__OrderDetail_ID: item.orderdetail__OrderDetail_ID,
              orderdetail__ProductBatch_ID__Supplier_ID: item.orderdetail__ProductBatch_ID__Supplier_ID,
              orderdetail__ProductBatch_ID__Supplier_ID__Supplier_Name: item.orderdetail__ProductBatch_ID__Supplier_ID__Supplier_Name,
              delivery__Dispatcher_ID: item.delivery__Dispatcher_ID,
              delivery__Dispatcher_ID__Dispatcher_Tel: item.delivery__Dispatcher_ID__Dispatcher_Tel,
              orderdetail__ProductBatch_ID__WareHouse_ID: item.orderdetail__ProductBatch_ID__WareHouse_ID,
            }]
          return newItem
        })
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
        case '奶类':
          return 'info'; // blue
        case '水果':
          return '#FFA07A'; // blue
        default:
          return 'info'; // blue
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
  Order_Time: string//下单时间
  Customer_ID__Customer_Name: string//客户姓名
  Order_Destination: string//收货地址
  orderdetail__ProductBatch_ID__Product_ID__Product_Type: string//产品类型（暂定）
  Customer_ID__Customer_Sex: string//客户性别
  Customer_ID__Customer_Tel: string//客户联系方式
  // address: string//客户联系方式
  orderdetail__OrderDetail_ID: string//订单明细编号
  // family:object//订单详细信息，一个列表，包含供应商编号
  "orderdetail__ProductBatch_ID__Supplier_ID": string
  "orderdetail__ProductBatch_ID__Supplier_ID__Supplier_Name": string
  "delivery__Dispatcher_ID": string
  "delivery__Dispatcher_ID__Dispatcher_Tel": string
  "orderdetail__ProductBatch_ID__WareHouse_ID": string
}

const tableRef = ref<TableInstance>()

const resetDateFilter = () => {
  tableRef.value!.clearFilter(['Order_Time'])
}
// TODO: improvement typing when refactor table
const clearFilter = () => {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-expect-error
  tableRef.value!.clearFilter()
}
const formatter = (row: User, column: TableColumnCtx<User>) => {
  return row.Order_Destination
}
const filterTag = (value: string, row: User) => {
  return row.orderdetail__ProductBatch_ID__Product_ID__Product_Type === value
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
