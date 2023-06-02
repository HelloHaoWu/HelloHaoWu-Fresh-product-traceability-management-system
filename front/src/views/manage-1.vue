<template>
  <div class = 'all_page'>
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
      <div id="main" style="width: 1650px;height:400px;"></div>
    </el-card>
    <div class = 'row3'>
      <el-card class="box-card3-1">
        <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>
      </el-card>
      <el-card class="box-card3-2" body-style="height: 320px; display: flex; justify-content:center; align-items:center">
<!--        <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>-->
        <div id="barchart" style="height: 200%; width: 100%;"></div>
      </el-card>
    </div>
  </div>
</template>



<style>
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
  mounted() {
    let myChart = echarts.init(document.getElementById('barchart'));//柱状图
    myChart.setOption(option);
    const chartIds = ['row1-1', 'row1-2', 'row1-3'];
    const optionIds = [option1,option2,option3]
    // console.log(option1)
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
        // console.log(this.selectedData)
        tempchart.setOption(this.getOption());
      });
    }
  },
  data() {
    let option0 = ref([]);option0 = reactive(option0)
    let option1 = ref([]);option1 = reactive(option1)
    let option2 = ref([]);option2 = reactive(option2)
    let option3 = ref([]);option3 = reactive(option3)
    let option = ref([]);option  = reactive(option)
    const getTableList = async () => {
      await axios.get('https://www.fastmock.site/mock/4adca991e257e0e3a89c8de7cad6295e/api/api/manage-1').then((res)=>{
        // await axios.get('http://43.143.167.222:8020/Testdata/').then((res)=>{
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
          value: this.selectedData['直接访问']>0 ? this.selectedData['直接访问'] : 0,
          name: '直接访问'
        },
        {
          value: this.selectedData['联盟广告']>0 ? this.selectedData['联盟广告'] : 0,
          name: '联盟广告'
        },
        {
          value: this.selectedData['搜索引擎']>0 ? this.selectedData['搜索引擎'] : 0,
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

let option00 = {
  "title": {
    "text": "my echarts"
  },
  "tooltip": {},
  "legend": {
    "data": [
      "肉类",
      "蔬菜",
      "蛋类"
    ]
  },
  "xAxis": {
    "data": [
      "A",
      "B",
      "C",
      "D",
      "E"
    ]
  },
  "yAxis": {},
  "series": [
    {
      "name": "肉类",
      "data": [
        10,
        22,
        28,
        43,
        49
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
        5,
        4,
        3,
        5,
        10
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
      "name": "蛋类",
      "data": [
        5,
        4,
        3,
        5,
        10
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
    }
  ]
}

let option11 = {
  "tooltip": {},
  "series": [
    {
      "type": "pie",
      "data": [
        {
          "value": 335,
          "name": "直接访问"
        },
        {
          "value": 234,
          "name": "联盟广告"
        },
        {
          "value": 1548,
          "name": "搜索引擎"
        }
      ]
    }
  ]
}

let option22 = {
  "tooltip": {},
  "series": [
    {
      "type": "pie",
      "data": [
        {
          "value": 335,
          "name": "直接访问"
        },
        {
          "value": 234,
          "name": "联盟广告"
        },
        {
          "value": 1548,
          "name": "搜索引擎"
        }
      ]
    }
  ]
}
let option33 = {
  "tooltip": {},
  "series": [
    {
      "type": "pie",
      "data": [
        {
          "value": 335,
          "name": "直接访问"
        },
        {
          "value": 234,
          "name": "联盟广告"
        },
        {
          "value": 1548,
          "name": "搜索引擎"
        }
      ]
    }
  ]
}
// 指定图表的配置项和数据
let option = {
  title: {
    text: 'my echarts'
  },
  tooltip: {},
  // 设置 legend，包含两个 data，分别对应两条线的名称
  // legend: {
  //   data: ['苹果', '梨子']
  // },
  xAxis: {
    data: ['A', 'B', 'C', 'D', 'E'],
    name: '', // 横坐标名称
    nameLocation: "middle" // 横坐标名称位置
  },
  yAxis: {
    name: '', // 纵坐标名称
    nameLocation: "middle", // 纵坐标名称位置
  },
  // 设置颜色数组
  color: ['#999999'],
  // 设置 series，分别设置两个数据系列的名称（name）、数据（data）、线条颜色等属性
  series: [
    {
      name: '现存量',
      data: [30, 12, 18, 23, 41],
      type: 'bar'
    }
  ]
};
</script>
