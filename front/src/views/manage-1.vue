<template>
  <div class = 'row1'>
    <el-card class="box-card1-1">
      <template #header>
        <div class="card-header">
          <span>Card name</span>
          <el-button class="button" text>Operation button</el-button>
        </div>
      </template>
      <div id="row1-1" style="width: 500px;height:400px;"></div>
    </el-card>
    <el-card class="box-card1-2">
      <template #header>
        <div class="card-header">
          <span>Card name</span>
          <el-button class="button" text>Operation button</el-button>
        </div>
      </template>
      <div id="row1-2" style="width: 500px;height:400px;"></div>
    </el-card>
    <el-card class="box-card1-3">
      <template #header>
        <div class="card-header">
          <span>Card name</span>
          <el-button class="button" text>Operation button</el-button>
        </div>
      </template>
      <div id="row1-3" style="width: 500px;height:400px;"></div>
    </el-card>
  </div>
  <el-card class="box-card2-1">
    <div id="main" style="width: 1600px;height:400px;"></div>
  </el-card>
  <div class = 'row3'>
    <el-card class="box-card3-1">
      <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>
    </el-card>
    <el-card class="box-card3-2">
      <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>
    </el-card>
  </div>
</template>



<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.row1{
  display:flex;
  margin-top: 20px;
  margin-left: -60px;
}
.box-card1-1 {
  flex-basis: 33%;
}
.box-card1-2 {
  flex-basis: 33%;
  margin-left: 10px;
}
.box-card1-3 {
  flex-basis: 33%;
  margin-left: 10px;
}
.box-card2-1 {
  margin-top: 30px;
  width : 1600px;
  margin-left: -60px;
}

.row3{
  display:flex;
  margin-top: 30px;
  margin-bottom: 20px;
  margin-left: -70px;
}

.box-card3-1 {
  flex-basis: 45%;
  margin-left: 10px;
  hieght :500px;
}
.box-card3-2 {
  flex-basis: 45%;
  margin-left: 10px;
  height: 500px;
}

</style>

<script type="ts">
import * as echarts from 'echarts';
import {ref, onMounted, defineComponent, reactive} from 'vue'
import axios from "axios";

export default defineComponent({
  mounted() {

    const chartIds = ['row1-1', 'row1-2', 'row1-3'];
    const optionIds = [option1,option2,option3]
    for (let i = 0;i <= chartIds.length - 1;i++)
    {
      let id = chartIds[i];
      let tempchart = echarts.init(document.getElementById(id));

      tempchart.setOption(optionIds[i]);
      // console.log(optionIds[i])
      tempchart.setOption(this.getOption());
      tempchart.on('legendselectchanged', (params) => {
        const {selected} = params;
        this.selectedData = selected;
        tempchart.setOption(this.getOption());
      });
    }
  },
  data() {
      let option0 = ref([]);option0 = reactive(option0)
      let option1 = ref([]);option1 = reactive(option1)
      let option2 = ref([]);option2 = reactive(option2)
      let option3 = ref([]);option3 = reactive(option3)
      const getTableList = async () => {
        await axios.get('https://www.fastmock.site/mock/4adca991e257e0e3a89c8de7cad6295e/api/api/manage-1').then((res)=>{
          option0.value = res.data.option0;console.log(res.data.option0)
          option1.value = res.data.option1;console.log(res.data.option1)
          option2.value = res.data.option2;console.log(res.data.option2)
          option3.value = res.data.option3;console.log(res.data.option3)

          let myChart = echarts.init(document.getElementById('main'));//折线图
          myChart.setOption(res.data.option0);
        })
      }
      onMounted(() => {
        getTableList()
      });
      return {
        selectedData: {
        '直接访问': true,
        '联盟广告': true,
        '搜索引擎': true
        }
      }
  },
    methods: {
      getOption() {
        const pieData = [
          {
            value: this.selectedData['直接访问'] ? 335 : 0,
            name: '直接访问'
          },
          {
            value: this.selectedData['联盟广告'] ? 234 : 0,
              name: '联盟广告'
          },
          {
            value: this.selectedData['搜索引擎'] ? 1548 : 0,
              name: '搜索引擎'
          }
      ];

        return {
          series: [
            {
              type: 'pie',
              data: pieData,
              itemStyle: {
                emphasis: {
                  scale: true
                }
              }
            }
          ],
          legend: {
            type: 'plain',
            selectedMode: 'multiple',
            selected: this.selectedData,
            data: ['直接访问', '联盟广告', '搜索引擎']
          }
        };
      }
    }
})
let option0 = {}
let option1 = {}
let option2 = {}
let option3 = {}
</script>

