<template>
  <div class = 'all_page'>
    <div class = 'deliverInform'><strong>供货单订单明细</strong></div>
    <el-card class = 'deliverTable'>
      <!--    <div class = 'deliverInform'>您的需配订单</div>-->
      <el-table
          :data="tableData"
          :default-sort="{ prop: 'date', order: 'descending' }"
          style="width: 100%"
      >
        <!--      <el-table-column prop="numberOfSupply" label="产品批次编号" sortable width="180" />-->
        <el-table-column prop="Product_ID_id" label="产品编号" width="180" />
        <el-table-column prop="WareHouse_ID_id" label="仓库编号" width="180" />
        <el-table-column prop="Supplier_ID_id" label="供应商编号" width="180" />
        <el-table-column prop="ProductBatch_Supply_Time" label="生产时间" width="180" />
        <el-table-column prop="ProductBatch_Warehousing_Time" label="入库时间" width="180"  />
        <!--      <el-table-column prop="statusOfProduct" label="订单状态" width="180"  />-->
        <el-table-column prop="ProductBatch_Supply_Amount" label="订单数量" width="180"  />
        <el-table-column prop="ProductBatch_Supply_Address" label="发出位置" width="180"  />
        <!--      <el-table-column prop="buttonText" label="按钮内容" width="180"  />-->
        <!--      <el-table-column>-->
        <!--        <template #default="scope">-->
        <!--          <el-button-->
        <!--              :class="{'active-button': scope.row.isActive, 'statusButton': !scope.row.isActive}"-->
        <!--              @click="changeStatusOfOrder(scope.$index,scope.row)">-->
        <!--            <strong>{{ scope.row.buttonText }}</strong>-->
        <!--            &lt;!&ndash;            :class是一个class类，其中的键绑定的是一个css对象，其对应的value值对应的是一个布尔类型对象，可以通过更改这个value来实现选择性css&ndash;&gt;-->
        <!--          </el-button>-->
        <!--        </template>-->
        <!--      </el-table-column>-->
      </el-table>
    </el-card>
  </div>
</template>

<style>
.all_page{
  margin-left: 80px;
}
.deliverTable{
  color: #111111;
  height: 700px;
  margin-top: 70px;
  padding: 0px;
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
import {reactive, ref ,onMounted,defineComponent} from 'vue'
import axios from "axios";//借用异步调用请求模块
export default defineComponent({
  data() {
    let tableData = ref([])
    tableData = reactive(tableData)

    //async即为axios中的模块之一，意为“异步”，其中的await函数可以实现功能
    const getTableList = async () => {
      await axios.get('https://www.fastmock.site/mock/4adca991e257e0e3a89c8de7cad6295e/api/api2').then((res)=>{
        // console.log(res.data.tableData);
        tableData.value = res.data.tableData
      })
    }
    const changeStatusOfOrder = (row_index: number, row: any) => {
      const targetRow = tableData.value[row_index];
      // 更新目标行的状态为已送达
      targetRow.statusOfOrder = '已送达'
      // 将被点击的按钮设置为激活状态
      row.isActive = true;
      // 更新按钮的显示文字为“订单已完成”
      targetRow.buttonText='订单已完成'
    };

    onMounted(() => {
      getTableList()
    });
    return {
      tableData,
      changeStatusOfOrder
    }
  }
})
</script>

<script lang="ts" setup>
import type { TableColumnCtx } from 'element-plus'
import {reactive} from "vue";
interface TableData {
  // numberOfSupply:string//产品批次编号
  Product_ID_id:string//产品编号
  WareHouse_ID_id:string//仓库编号
  Supplier_ID_id:string//供应商编号
  ProductBatch_Supply_Time:string//生产时间
  ProductBatch_Warehousing_Time:string//入库时间
  // statusOfProduct:string//订单状态
  ProductBatch_Supply_Amount: string//订单数量
  ProductBatch_Supply_Address:string//发出位置
  // buttonText: string//按钮内容
}

// const formatter = (row: TableData, column: TableColumnCtx<TableData>) => {
//   return row.targetAddress
// }


</script>

