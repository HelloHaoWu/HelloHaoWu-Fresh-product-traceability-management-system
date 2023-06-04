<template>
  <div class = 'all_page'>
    <div class = 'deliverInform'><strong>您的需配订单</strong></div>
      <el-card class = 'deliverTable'>
        <el-table
            :data="tableData"
            :default-sort="{ prop: 'date', order: 'descending' }"
            style="width: 100%"
            class = 'myform'
        >
          <el-table-column prop="Dispatcher_ID" label="配送编号" sortable width="100" />
          <el-table-column prop="Order_ID" label="订单编号" width="100" />
          <el-table-column prop="Order_ID__orderdetail__ProductBatch_ID__ProductBatch_Expiration_Time" label="最晚送达时间" width="180" />
          <el-table-column prop="Completion_Time" label="完成时间" width="220" />
          <el-table-column prop="Vehicle_ID" label="车辆编号" width="180" />
          <el-table-column prop="Order_ID__Order_Destination" label="目标位置" width="220" />
          <el-table-column prop="Current_Status" label="订单状态" width="180"  />
          <el-table-column>
            <template #default="scope">
              <el-button
                  :class="{'active-button': scope.row.isActive, 'statusButton': !scope.row.isActive}"
                  @click="changeStatusOfOrder(scope.$index,scope.row)">
                <strong>{{ scope.row.buttonText }}</strong>
<!--                    <div class = 'mytext'>-->
<!--                      <strong>订单未送达</strong>-->
<!--                    </div>-->
<!--                等待post请求-->
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
  </div>
</template>

<style>
.myform{
  height: 800px;
  overflow: auto;
  position: relative;
}
.all_page{
  margin-left: 80px;
}
.deliverTable{
  color: #111111;
  height: 700px;
  margin-top: 70px;
  /*margin-right: 50px;*/
  margin-left: -80px;
  margin-right: 30px;

}
/*.statusButton{*/
/*  width: 120px;*/
/*  background-color: red;*/
/*  opacity: 0.7;*/
/*  color: black;*/
/*  font-size: 14px;*/
/*}*/
.statusButton{
  width: 120px;
  background: #B0C4DE;
  opacity: 0.9;
  color: #333333;
}
.active-button {
  width: 120px;
  background: #B0C4DE;
  opacity: 0.9;
  color: #333333;
}
.deliverInform{
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
      await axios.get('http://43.143.167.222:8020/Delivery/').then((res)=>{
          // console.log(res.data);
          tableData.value = res.data.map(item => {
            if (item.Current_Status === 2) {
              return {...item, buttonText: '已送达'}
            } else {
              return {...item, buttonText: '订单未送达'}
            }
          })
      }
    )}
    onMounted(() => {
      getTableList()
    });
    const changeStatusOfOrder = (row_index: number, row: any) => {
      const targetRow = tableData.value[row_index];
      targetRow.Current_Status = '2';
      const completionTime = new Date().toISOString(); // 获取系统当前时间
      targetRow.Completion_Time = completionTime; // 修改 Completion_Time 属性
      row.isActive = true;
      targetRow.buttonText = '已送达';
      // 其他操作
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
  Delivery_ID:string//配送编号
  Order_ID_id:string//订单编号
  Latest_Delivery_Time:string//最晚送达时间或送达时间
  Current_Status:string//订单状态
  Vehicle_ID_id: string//车辆编号
  // realLocation:string//实时位置
  // address: string//目标地址
  buttonText: string//按钮内容
}

// const formatter = (row: TableData, column: TableColumnCtx<TableData>) => {
//   return row.realLocation
// }

</script>

