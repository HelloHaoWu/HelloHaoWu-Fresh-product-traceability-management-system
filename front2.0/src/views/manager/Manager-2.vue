<template>
  <div class = 'all_page'>
    <div class = 'orderInform'><strong>订单desu</strong></div>
    <el-card class = 'orderTable'>
      <el-table
          :data="tableData"
          :default-sort="{ prop: 'date', order: 'descending' }"
          style="width: 100%"
      >
        <el-table-column prop="orderdetail__OrderDetail_ID" label="订单编号" width="180" sortable/>
        <el-table-column prop="Delivery_ID" label="配送编号" width="180" sortable/>
        <el-table-column prop="Customer_ID" label="用户编号" width="180" sortable/>
        <el-table-column prop="Order_Destination" label="用户地址" width="180" sortable/>
        <el-table-column prop="Latest_Delivery_Time" label="最晚送达时间/送达时间" width="180" sortable/>
        <el-table-column prop="Vehicle_ID_id" label="车辆编号" width="180" sortable/>
  <!--      <el-table-column prop="realLocation" label="实时位置" width="180" sortable/>-->
        <el-table-column prop="Current_Status" label="订单状态" width="180"  sortable/>

      </el-table>
    </el-card>
  </div>
</template>

<style>
.all_page{
  margin-left: 80px;
}

.orderTable{
  color: #111111;
  height: 700px;
  margin-top: 70px;
  /*margin-right: 50px;*/
  margin-left: -80px;
  margin-right: 30px;

}
.orderInform{
  font-size: 20px;
  margin-left: -80px;
  margin-bottom: -40px;
}
</style>

<script lang="ts">
import {ref, onMounted, defineComponent, reactive} from 'vue'
import axios from "axios";
export default defineComponent({
  data() {
    let tableData = ref([])
    tableData = reactive(tableData)

    const getTableList = async () => {
      await axios.get('https://www.fastmock.site/mock/4adca991e257e0e3a89c8de7cad6295e/api/api').then((res)=>{
        console.log(res.data.tableData);
        tableData.value = res.data.tableData
      })
    }
    onMounted(() => {
      getTableList()
    });
    const changeStatusOfOrder = (row_index: number, row: any) => {
      const targetRow = tableData.value[row_index];
      targetRow.statusOfOrder = '已送达'
      row.isActive = true;
      targetRow.buttonText='订单已完成'
    };


    return {
      tableData,
      changeStatusOfOrder,
    }
  }
})
</script>

<script lang="ts" setup>
import type { TableColumnCtx } from 'element-plus'
import {reactive} from "vue";
interface TableData {
  orderdetail__OrderDetail_ID: string//订单明细编号
  Delivery_ID:string//配送编号
  Customer_ID:string//用户编号
  Order_Destination:string//用户地址
  Latest_Delivery_Time:string//最晚送达时间或送达时间
  Current_Status:string//订单状态
  Vehicle_ID_id: string//车辆编号
  // realLocation:string//实时位置
  // address: string//目标地址
  // buttonText: string//按钮内容
}

// const formatter = (row: TableData, column: TableColumnCtx<TableData>) => {
//   return row.realLocation
// }

</script>

