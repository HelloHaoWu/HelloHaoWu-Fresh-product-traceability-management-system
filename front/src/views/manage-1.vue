<template>
  <div class = 'all_page'>
    <div class = 'row1'>
      <el-card class="box-card1-1">
        <template #header>
          <div class="card-header">
            <span>北京顺义仓</span>
<!--            <el-button class="button" text>Operation button</el-button>-->
          </div>
        </template>
        <div id="row1-1" style="width: 500px;height:400px;"></div>
      </el-card>
      <el-card class="box-card1-2">
        <template #header>
          <div class="card-header">
            <span>北京昌平1仓</span>
<!--            <el-button class="button" text>Operation button</el-button>-->
          </div>
        </template>
        <div id="row1-2" style="width: 500px;height:400px;"></div>
      </el-card>
      <el-card class="box-card1-3">
        <template #header>
          <div class="card-header">
            <span>天津滨海仓</span>
<!--            <el-button class="button" text>Operation button</el-button>-->
          </div>
        </template>
        <div id="row1-3" style="width: 500px;height:400px;"></div>
      </el-card>
    </div>
    <el-card class="box-card2-1">
      <div id="main" style="width: 1650px;height:400px;"></div>
    </el-card>
    <div class = 'row3'>
      <div class = 'myform'>
        <el-card class="box-card3-1">
          <el-table
              :data="tableData"
              :default-sort="{ prop: 'date', order: 'descending' }"
              style="width: 100%"
          >
            <el-table-column prop="订单ID" label="订单ID" sortable width="180" />
            <el-table-column prop="订购者" label="订购者" width="180" />
            <el-table-column prop="下单时间" label="下单时间" width="180" />
            <el-table-column prop="订单状态" label="订单状态" width="180" />
          </el-table>
        </el-card>
      </div>
      <el-card class="box-card3-2" body-style="height: 320px; display: flex; justify-content:center; align-items:center">
<!--        <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>-->
        <div id="barchart" style="height: 200%; width: 100%;" class="barchart"></div>
      </el-card>
    </div>
  </div>
</template>



<style>
.myform{
  height: 400px;
  overflow: auto;
  position: relative;
}
.barchart{
  margin-top: 20px;
}
.all_page{
  /*display:flex;*/
  margin-left: 50px;
}
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
  margin-right: 60px;
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
  margin-right: 1000px;
}

.row3{
  display:flex;
  margin-top: 30px;
  margin-bottom: 20px;
  margin-left: -70px;
  margin-right: -63px;
}

.box-card3-1 {
  flex-basis: 45%;
  margin-left: 10px;
  hieght :500px;
}
.box-card3-2 {
  margin_top : 200px;
  flex-basis: 45%;
  margin-left: 40px;
  height: 430px;
  /* 新增样式 */
  width: calc(45% - 10px);
  margin-right: 10px;
  padding-left: 60px; /* 增加左侧padding */
}

</style>

<script type="ts">
import * as echarts from 'echarts';
import {ref, onMounted, defineComponent, reactive} from 'vue'
import axios from "axios";
// import {log} from "echarts/types/src/util/log";

export default defineComponent({
  // created() {
  //   this.getTableList();
  // },
  mounted() {
    const chartIds = ['row1-1', 'row1-2', 'row1-3'];
    // console.log(option1)
    for (let i = 0;i <= chartIds.length - 1;i++)
    {
      let id = chartIds[i];
      let tempchart = echarts.init(document.getElementById(id));

      // console.log(optionIds[i])
      tempchart.setOption(this.getOption());
      tempchart.on('legendselectchanged', (params) => {
        const {selected} = params;
        this.selectedData = selected;
        if (!Object.keys(this.selectedData).length) {
          this.selectedData = {};
        }
        tempchart.setOption(this.getOption());
      });
    }
  },

  data() {
    const getTableList = async () => {
      //饼图
      await axios.get('http://43.143.167.222:8020/Piedata_sub/').then((res) => {
        this.option1.series[0].data = res.data.piedata1
        this.option2.series[0].data = res.data.piedata2;
        this.option3.series[0].data = res.data.piedata3;
        const chartIds = ['row1-1', 'row1-2', 'row1-3'];
        for (let i = 0; i < chartIds.length; i++) {
          const id = chartIds[i];
          const tempchart = echarts.init(document.getElementById(id));
          // console.log(this[`option${i+1}`])
          tempchart.setOption(this[`option${i + 1}`]);
        }
      })
      //折线图
      await axios.get('http://43.143.167.222:8020/Linechart/').then((res) => {
        // option0.value = res.data.option0;console.log(res.data.option0)
        //   console.log(res.data)
        this.option0.legend.data = res.data.legend
        this.option0.xAxis.data = res.data.xAxis
        this.option0.legend.data = res.data.legend

        this.option0.series[0].name = res.data.line1.name
        this.option0.series[0].data = res.data.line1.data
        this.option0.series[1].name = res.data.line2.name
        this.option0.series[1].data = res.data.line2.data
        this.option0.series[2].name = res.data.line3.name
        this.option0.series[2].data = res.data.line3.data
        this.option0.series[3].name = res.data.line4.name
        this.option0.series[3].data = res.data.line4.data
        this.option0.series[4].name = res.data.line5.name
        this.option0.series[4].data = res.data.line5.data

        let myChart = echarts.init(document.getElementById('main'));//折线图
        myChart.setOption(this.option0);
      })
      //柱状图
      await axios.get('http://43.143.167.222:8020/form1/').then((res) => {
        // console.log(res.data[0].库存总量)
        this.option.xAxis.data[0] = res.data[0].生鲜种类
        this.option.series[0].data[0].value = res.data[0].库存总量
        this.option.xAxis.data[1] = res.data[1].生鲜种类
        this.option.series[0].data[1].value = res.data[1].库存总量
        this.option.xAxis.data[2] = res.data[2].生鲜种类
        this.option.series[0].data[2].value = res.data[2].库存总量
        this.option.xAxis.data[3] = res.data[3].生鲜种类
        this.option.series[0].data[3].value = res.data[3].库存总量
        this.option.xAxis.data[4] = res.data[4].生鲜种类
        this.option.series[0].data[4].value = res.data[4].库存总量

        let myChart = echarts.init(document.getElementById('barchart'));//柱状图
        myChart.setOption(this.option);
      })

      //form
      await axios.get('http://43.143.167.222:8020/form2/').then((res) => {
        this.tableData = res.data
        console.log(this.tabledata[0])
      })
    }
    onMounted(() => {
      getTableList()
    });
    return {

      option : {
        title: {
          text: 'my echarts'
        },
        tooltip: {},
        xAxis: {
          data: [],
          name: '', // 横坐标名称
          nameLocation: "middle" // 横坐标名称位置
        },
        yAxis: {
          name: '', // 纵坐标名称
          nameLocation: "middle", // 纵坐标名称位置
        },
        series: [
          {
            name: '现存量',
            data: [
                { value: 0, itemStyle: { color: '#007bff' } },
                { value: 0, itemStyle: { color: '#dc3545' } },
                { value: 0, itemStyle: { color: '#6c757d' } },
                { value: 0, itemStyle: { color: '#28a745' } },
                { value: 0, itemStyle: { color: '#343a40' } }
            ],
            type: 'bar',
            color: '#007bff'
          }
        ],

      },
      option0 : {
        "title": {
          "text": "近五天销量"
        },
        "tooltip": {},
        "legend": {
          "data": []
        },
        "xAxis": {
          "data": [
          ]
        },
        "yAxis": {},
        "series": [
          {
            "name": "肉类",
            "data": [

            ],
            "type": "line",
            "stack": "x",
            "itemStyle": {
              "color": "red"
            },
            "emphasis": {
              "itemStyle": {
                "color": "red"
              }
            }
          },
          {
            "name": "蔬菜",
            "data": [

            ],
            "type": "line",
            "stack": "x",
            "itemStyle": {
              "color": "green"
            },
            "emphasis": {
              "itemStyle": {
                "color": "green"
              }
            }
          },
          {
            "name": "奶类",
            "data": [

            ],
            "type": "line",
            "stack": "x",
            "itemStyle": {
              "color": "grey"
            },
            "emphasis": {
              "itemStyle": {
                "color": "grey"
              }
            }
          },
          {
            "name": "水果",
            "data": [

            ],
            "type": "line",
            "stack": "x",
            "itemStyle": {
              "color": "blue"
            },
            "emphasis": {
              "itemStyle": {
                "color": "blue"
              }
            }
          },
          {
            "name": "其他",
            "data": [
            ],
            "type": "line",
            "stack": "x",
            "itemStyle": {
              "color": "black"
            },
            "emphasis": {
              "itemStyle": {
                "color": "black"
              }
            }
          }
        ]
      },
      option1: ref({
        "tooltip": {},
        "series": [{
          "type": "pie",
          "data": [
          ],
        }]
      }),
      option2: ref({
        "tooltip": {},
        "series": [{
          "type": "pie",
          "data": [],
        }]
      }),
      option3: ref({
        "tooltip": {},
        "series": [{
          "type": "pie",
          "data": [],
        }]
      }),
      selectedData: {
        '肉类': true,
        '蔬菜': true,
        '水果': true,
        '奶类': true,
      },
      tabledata:ref([])
    }

  },
  methods: {
    getOption() {
      const pieData = [
        {
          value: this.selectedData['肉类']>0 ? this.selectedData['肉类'] : 0,
          name: '肉类'
        },
        {
          value: this.selectedData['水果']>0 ? this.selectedData['水果'] : 0,
          name: '蛋类'
        },
        {
          value: this.selectedData['奶类']>0 ? this.selectedData['奶类'] : 0,
          name: '奶类'
        },
        {
          value: this.selectedData['蔬菜']>0 ? this.selectedData['蔬菜'] : 0,
          name: '蔬菜'
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
          data: ['肉类','水果','奶类','蔬菜']
        }
      };
    }
  }
})
</script>
