<template>
  <div class = 'all_page'>
    <div class = 'stockInform'><strong>库存desu</strong></div>
    <el-card class = 'stockTable'>
      <el-table
          :data="tableData"
          :default-sort="{ prop: 'date', order: 'descending' }"
          style="width: 100%"
      >
        <!--      <el-table-column prop="numberOfBatch" label="批次编号" width="180" sortable/>-->
        <el-table-column prop="Product_ID_id" label="产品编号" width="180" sortable/>
        <el-table-column prop="WareHouse_ID_id" label="仓库编号" width="180" sortable/>
        <el-table-column prop="Supplier_ID_id" label="供应商编号" width="180" sortable/>
        <el-table-column prop="orderdetail__ProductBatch_ID__Product_ID__Product_Type" label="种类" width="180" sortable
                         :filters="[
                              { text: '蔬菜', value: '蔬菜' },
                              { text: '肉类', value: '肉类' },
                              { text: '海鲜', value: '海鲜' },
                              { text: '蛋类', value: '蛋类' },
                            ]"
                         :filter-method="filterHandler"/>
        <el-table-column prop="ProductBatch_Supply_Amount" label="入库量" width="180" sortable/>
        <el-table-column prop="ProductBatch_Warehousing_Time" label="入库时间" width="180" sortable/>
        <el-table-column prop="ProductBatch_Expiration_Time" label="到期时间" width="180" sortable/>
      </el-table>
    </el-card>
  </div>
</template>

<style>
.all_page{
  margin-left: 80px;
}
.stockTable{
  color: #111111;
  height: 700px;
  margin-top: 70px;
  /*margin-right: 50px;*/
  margin-left: -80px;
  margin-right: 30px;

}
.stockInform{
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

  // numberOfBatch:string//批次编号
  Product_ID_id:string//产品编号
  WareHouse_ID_id:string//仓库编号
  Supplier_ID_id:string//供应商编号
  orderdetail__ProductBatch_ID__Product_ID__Product_Type:string//种类
  ProductBatch_Supply_Amount: string//订单数量
  ProductBatch_Warehousing_Time:string//入库时间
  ProductBatch_Expiration_Time:string//到期时间
}


</script>

