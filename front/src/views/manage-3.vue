<template>
  <div class='total_ware'>
    <div class='stockInform'><strong>库存总览</strong></div>
    <el-card class='stockTable'>
      <el-table
          :data="tableData"
          :default-sort="{ prop: 'date', order: 'descending' }"
          style="width: 100%"
          class = 'myform_ware'
      >
        <el-table-column prop="ProductBatch_ID" label="批次编号" width="180" sortable/>
        <el-table-column prop="Product_ID__Product_Name" label="产品名称" width="180" sortable/>
        <el-table-column prop="WareHouse_ID__WareHouse_Name" label="仓库名称" width="180" sortable/>
        <el-table-column prop="Supplier_ID__Supplier_Name" label="供应商名称" width="180" sortable/>
        <el-table-column prop="Product_ID__Product_Type" label="种类" width="180" sortable
                         :filters="[
                              { text: '蔬菜', value: '蔬菜' },
                              { text: '肉类', value: '肉类' },
                              { text: '水果', value: '水果' },
                              { text: '奶类', value: '奶类' },
                            ]"
                         :filter-method="filterHandler"/>
        <el-table-column prop="ProductBatch_Supply_Amount" label="入库量" width="180" sortable/>
        <el-table-column prop="ProductBatch_Warehousing_Time" label="入库时间" width="180" sortable/>
        <el-table-column prop="ProductBatch_Expiration_Time" label="过期时间" width="180" sortable/>
      </el-table>
    </el-card>
  </div>
</template>

<style>
.myform_ware{
  height: 800px;
  overflow: auto;
  position: relative;
}
.total_ware{
  margin-left: 14vh;
  margin-right: 2vh;
  margin-top: 4vh;
}
.stockTable{
  color: #111111;
  height: 85vh;
  margin-top: 7vh;
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
      await axios.get('http://43.143.167.222:8020/Manager3/').then((res)=>{
        console.log(res.data);
        tableData.value = res.data;
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

const filterHandler = (
    value: string,
    row: TableData,
    column: TableColumnCtx<TableData>
) => {
  const property = column['property']
  return row[property] === value
}
</script>

