<template>
  <div class = 'deliverInform'><strong>您的需配订单</strong></div>
  <el-card class = 'deliverTable'>
    <el-table
        :data="tableData"
        :default-sort="{ prop: 'date', order: 'descending' }"
        style="width: 100%"
    >
      <el-table-column prop="numberOfDelivery" label="配送编号" sortable width="180" />
      <el-table-column prop="numberOfOrder" label="订单编号" width="180" />
      <el-table-column prop="lastestTime" label="最晚送达时间/送达时间" width="180" />
      <el-table-column prop="numberOfVan" label="车辆编号" width="180" />
      <el-table-column prop="realLocation" label="实时位置" width="180" />
      <el-table-column prop="statusOfOrder" label="订单状态" width="180"  />
      <el-table-column>
        <template #default="scope">
          <el-button
              :class="{'active-button': scope.row.isActive, 'statusButton': !scope.row.isActive}"
              @click="changeStatusOfOrder(scope.$index,scope.row)">
            <strong>{{ scope.row.buttonText }}</strong>
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-card>
</template>

<style>
.deliverTable{
  color: #111111;
  height: 700px;
  margin-top: 70px;
  /*margin-right: 50px;*/
  margin-left: -80px;
  margin-right: 30px;

}
.statusButton{
  width: 120px;
  background-color: red;
  opacity: 0.7;
  color: black;
  font-size: 14px;
}
.active-button {
  width: 120px;
  background: #B0C4DE;
  opacity: 0.6;
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
  numberOfDelivery:string//配送编号
  numberOfOrder:string//订单编号
  lastestTime:string//最晚送达时间或送达时间
  statusOfOrder:string//订单状态
  numberOfVan: string//车辆编号
  realLocation:string//实时位置
  // address: string//目标地址
  buttonText: string//按钮内容
}

const formatter = (row: TableData, column: TableColumnCtx<TableData>) => {
  return row.realLocation
}

</script>

