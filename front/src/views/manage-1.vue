<template>
  <div class='all_page'>
    <div class="graph-home">
      <el-card class='warehouse1' style="height: 300px; margin-right: 15px">
        <div ref="echarts1" style="height: 260px; width: 100%"></div>
      </el-card>
      <el-card class='warehouse2' style="height: 300px; margin-left: 15px; margin-right: 15px">
        <div ref="echarts2" style="height: 260px; width: 100%"></div>
      </el-card>
      <el-card class='warehouse3' style="height: 300px; margin-left: 15px">
        <div ref="echarts3" style="height: 260px; width: 100%"></div>
      </el-card>
    </div>
    <el-card class="line_chart">
      <div ref="echarts_line" style="height: 350px; width: 100%"></div>
    </el-card>
    <div class="foot-home">
      <el-card class="el-card-latest">
        <table class="table-home">
          <thead class="thead-home">
          <tr class="tr-home">
            <th class="th-home-first">订单ID</th>
            <th class="th-home">订购者</th>
            <th class="th-home">下单时间</th>
            <th class="th-home">订单状态</th>
          </tr>
          </thead>
          <tbody class="tbody-home">
          <tr class="tr-home" v-for="item in Lastorder" :key="item.id">
            <td class="UserHash-home">{{ item.id }}</td>
            <td class="tdothers-home">{{ item.order }}</td>
            <td class="tdothers-home">{{ item.orderdate }}</td>
            <td class="tdothers-home">
              <!--                  {{ item.status }}-->
              <!-- .json文件传给vue3前端的数据标题不能带"-"，即.json数据的标题不能带"-" -->
              <el-tag style="height: 30px; width: 65px" :type="Judge_status(item.orderstatus)">{{ item.orderstatus }}</el-tag>
            </td>
          </tr>
          <el-pagination layout="prev, pager, next" :current-page=this.current_page :total="total" :page-size=6 @current-change="handlePage"/>
          </tbody>
        </table>
      </el-card>
      <div class="el-card-showpicture">
        <el-card class='pill_chart' style="margin-left: 15px;">
          <div ref="pillecharts" style="height: 47vh; width: 100%"></div>
        </el-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import * as echarts from 'echarts'
// ↓导入检测元素尺寸(resize)变化的库, 从而进行图表尺寸的自适应
import elementResizeDetectorMaker from 'element-resize-detector'
// ↓日期选择页
const erd = elementResizeDetectorMaker()
export default {
  name: "AppHome",
  // ↓尝试将画图方法抛出, 在外部调用
  // provide () {
  //   return {
  //     loadechartsdata: this.loadechartsdata,
  //     loadTransNode: this.loadTransNode,
  //     loadLabelNum: this.loadLabelNum
  //   }
  // },
  data() {
    return {
      Lastorder: [], // 最近的订单
      echartsline: [], // 折线图
      echart1: [], // 饼图1
      echart2: [], // 饼图2
      echart3: [], // 饼图3
      current_page: 1, // 当前页
      total: 0, // 总信息条数
      pageData: {
        page: 1,
        limit: 6
      },
      pillar: [] // 柱状图
    }
  },
  created() {
    this.pillload()
    this.loadorders()
    this.loadlinedata()
    this.loadpiedata1()
    this.loadpiedata2()
    this.loadpiedata3()
  },
  methods: {
    pillload() {
      axios
          .get('http://43.143.167.222:8020/form1/')
          .then(res => {
            this.pillar = res.data
            const pillardata = this.pillar
            const echartpill = echarts.init(this.$refs.pillecharts)
            var pilloption = {
              title: {
                text: '各类产品当前总库存量',
                left: 'center' // 设置标题居中
              },
              xAxis: {
                type: 'category',
                data: [pillardata[0]['生鲜种类'], pillardata[1]['生鲜种类'], pillardata[2]['生鲜种类'], pillardata[3]['生鲜种类'], pillardata[4]['生鲜种类']]
              },
              yAxis: {
                type: 'value'
              },
              tooltip: {
                trigger: 'item'
              },
              series: [
                {
                  data: [
                    {
                      value: pillardata[0]['库存总量'],
                      itemStyle: {
                        color: '#91cc75'
                      }
                    },
                    {
                      value: pillardata[1]['库存总量'],
                      itemStyle: {
                        color: '#5470c6'
                      }
                    },
                    {
                      value: pillardata[2]['库存总量'],
                      itemStyle: {
                        color: '#fac858'
                      }
                    },
                    {
                      value: pillardata[3]['库存总量'],
                      itemStyle: {
                        color: '#fc8452'
                      }
                    },
                    {
                      value: pillardata[4]['库存总量'],
                      itemStyle: {
                        color: '#ee6666'
                      }
                    }],
                  type: 'bar'
                }
              ]
            }
            echartpill.setOption(pilloption)
            erd.listenTo(document.querySelector(".pill_chart"), () => {
              echartpill.resize()
            })
          })
    },
    handlePage(val) {
      console.log(val)
      this.pageData.page = val
      this.current_page = val
      this.loadorders()
    },
    Judge_status(status) { // 渲染状态色
      if (status === "未发货") {
        return 'warning'
      } else if (status === "配送中") {
        return ''
      } else {
        return 'success'
      }
    },
    loadorders() {
      axios
          .get('http://43.143.167.222:8020/form2/')
          .then(res => {
            this.total = res.data.length || 0
            console.log(this.list)
            // 只显示前6个
            this.Lastorder = []
            for(let i=(this.pageData.page-1)*this.pageData.limit, j=0; j < this.pageData.limit; i++) {
              this.Lastorder[j] = res.data[i];
              j++;
              if (i === res.data.length - 1) {
                break
              }
            }
          })
    },
    loadlinedata() {
      axios
          .get('http://43.143.167.222:8020/Linechart/')
          .then(res => {
            this.echartsline = res.data
            const linedata = this.echartsline
            const echartline = echarts.init(this.$refs.echarts_line)
            var lineoption = {
              title: {
                text: '近4日各类产品销量趋势'
              },
              tooltip: {
                trigger: 'axis'
              },
              legend: {
                data: linedata['legend']
              },
              grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
              },
              toolbox: {
                feature: {
                  saveAsImage: {}
                }
              },
              xAxis: {
                type: 'category',
                boundaryGap: false,
                data: linedata['xAxis']
              },
              yAxis: {
                type: 'value'
              },
              series: [
                {
                  name: linedata['line1']['name'],
                  type: 'line',
                  stack: 'Total',
                  data: linedata['line1']['data']
                },
                {
                  name: linedata['line2']['name'],
                  type: 'line',
                  stack: 'Total',
                  data: linedata['line2']['data']
                },
                {
                  name: linedata['line3']['name'],
                  type: 'line',
                  stack: 'Total',
                  data: linedata['line3']['data']
                },
                {
                  name: linedata['line4']['name'],
                  type: 'line',
                  stack: 'Total',
                  data: linedata['line4']['data']
                },
                {
                  name: linedata['line5']['name'],
                  type: 'line',
                  stack: 'Total',
                  data: linedata['line5']['data']
                }
              ]
            }
            echartline.setOption(lineoption)
            erd.listenTo(document.querySelector(".line_chart"), () => {
              echartline.resize()
            })
          })
    },
    loadpiedata1() {
      axios
          .get('http://43.143.167.222:8020/Piedata_sub/')
          .then(res => {
            this.echart1 = res.data['piedata1']
            const piedata1 = this.echart1
            const echarts1 = echarts.init(this.$refs.echarts1)
            var echart1option = {
              title: {
                text: '北京顺义仓储'
              },
              tooltip: {
                trigger: 'item'
              },
              legend: {
                orient: 'vertical',
                top: 50,
                right: 5
              },
              color: ['rgb(228, 153, 182)', 'rgb(216, 122, 128)', 'rgb(255, 185, 128)', 'rgb(182, 162, 222)'],
              series: [
                {
                  name: '该类商品仓储量',
                  type: 'pie',
                  radius: ['40%', '70%'],
                  avoidLabelOverlap: true,
                  itemStyle: {
                    borderRadius: 6,
                    borderColor: '#fff',
                    borderWidth: 2
                  },
                  center: ['38%', '58%'],
                  data: [
                    // ↓此处第一条"arknet_market"有数据造假, 请在真实部署时修改
                    { value: piedata1[0]['value'], name: piedata1[0]['name'] },
                    { value: piedata1[1]['value'], name: piedata1[1]['name'] },
                    { value: piedata1[2]['value'], name: piedata1[2]['name'] },
                    { value: piedata1[3]['value'], name: piedata1[3]['name'] },
                  ],
                  grid: {
                    top: '12%',
                    left: '-0.1%',
                    // right: '4%',
                    bottom: '15%',
                    containLabel: true
                  },
                }
              ]
            }
            echarts1.setOption(echart1option)
            erd.listenTo(document.querySelector(".warehouse1"), () => {
              echarts1.resize()
            })
          })
    },
    loadpiedata2() {
      axios
          .get('http://43.143.167.222:8020/Piedata_sub/')
          .then(res => {
            this.echart2 = res.data['piedata2']
            const piedata2 = this.echart2
            const echarts2 = echarts.init(this.$refs.echarts2)
            var echart2option = {
              title: {
                text: '北京昌平1仓储'
              },
              tooltip: {
                trigger: 'item'
              },
              legend: {
                orient: 'vertical',
                top: 50,
                right: 5
              },
              color: ['rgb(228, 153, 182)', 'rgb(216, 122, 128)', 'rgb(255, 185, 128)'],
              series: [
                {
                  name: '该类商品仓储量',
                  type: 'pie',
                  radius: ['40%', '70%'],
                  avoidLabelOverlap: true,
                  itemStyle: {
                    borderRadius: 6,
                    borderColor: '#fff',
                    borderWidth: 2
                  },
                  center: ['38%', '58%'],
                  data: [
                    // ↓此处第一条"arknet_market"有数据造假, 请在真实部署时修改
                    { value: piedata2[0]['value'], name: piedata2[0]['name'] },
                    { value: piedata2[1]['value'], name: piedata2[1]['name'] },
                    { value: piedata2[2]['value'], name: piedata2[2]['name'] },
                  ],
                  grid: {
                    top: '12%',
                    left: '-0.1%',
                    // right: '4%',
                    bottom: '15%',
                    containLabel: true
                  },
                }
              ]
            }
            echarts2.setOption(echart2option)
            erd.listenTo(document.querySelector(".warehouse2"), () => {
              echarts2.resize()
            })
          })
    },
    loadpiedata3() { // 已经改完
      axios
          .get('http://43.143.167.222:8020/Piedata_sub/')
          .then(res => {
            this.echart3 = res.data['piedata3']
            const piedata3 = this.echart3
            const echarts3 = echarts.init(this.$refs.echarts3)
            var echart3option = {
              title: {
                text: '天津滨海仓储'
              },
              tooltip: {
                trigger: 'item'
              },
              legend: {
                orient: 'vertical',
                top: 50,
                right: 5
              },
              color: ['rgb(228, 153, 182)', 'rgb(216, 122, 128)', 'rgb(255, 185, 128)'],
              series: [
                {
                  name: '该类商品仓储量',
                  type: 'pie',
                  radius: ['40%', '70%'],
                  avoidLabelOverlap: true,
                  itemStyle: {
                    borderRadius: 6,
                    borderColor: '#fff',
                    borderWidth: 2
                  },
                  center: ['38%', '58%'],
                  data: [
                    // ↓此处第一条"arknet_market"有数据造假, 请在真实部署时修改
                    { value: piedata3[0]['value'], name: piedata3[0]['name'] },
                    { value: piedata3[1]['value'], name: piedata3[1]['name'] },
                    { value: piedata3[2]['value'], name: piedata3[2]['name'] },
                  ],
                  grid: {
                    top: '12%',
                    left: '-0.1%',
                    // right: '4%',
                    bottom: '15%',
                    containLabel: true
                  },
                }
              ]
            }
            echarts3.setOption(echart3option)
            erd.listenTo(document.querySelector(".warehouse3"), () => {
              echarts3.resize()
            })
          })
    },
  },
}
</script>

<style lang="less">
.all_page{
  /*display:flex;*/
  margin-left: 6vh;
  margin-right: 6vh;
}
.graph-home {
  margin-top: 4vh;
  display: flex;
  justify-content: space-between;
  .el-card {
    width: 32%;
  }
}
.line_chart {
  margin-top: 3vh;
  margin-right: 6vh;
  width: 100%;
}
.foot-home {
  justify-content: space-between;
  margin-top: 30px;
  margin-bottom: 40px;
  width: 100%;
  display: flex;
  height: 48vh;
  max-height: 48vh;
  .el-card-latest {
    width: 60%;
    //height: 50vh;
    text-align: center;
    font-size: 14px;
  }
  .el-card-showpicture {
    width: 38.3%;
    .pill_chart {
      height: 100%;
    }
  }
}
.table-home {
  align-content: center;
  // ↓表示表格的两边框合并为一条
  border-collapse: collapse;
  width: 100%;
  // ↓将界面设置为无边框
  border: none;
}
.th-home-first {
  // ↓将界面设置为无边框
  border: none;
  // ↓将界面设置为仅有底边框
  border-bottom: 1px solid #cccccc;
  // ↓水平居中
  text-align: left;
  padding: 8px 8px 8px 16px; // 上 右 下 左
  background-color: white;
  color: #666666;
  height: 45px;
  width: 10%;
}
.th-home {
  // ↓将界面设置为无边框
  border: none;
  // ↓将界面设置为仅有底边框
  border-bottom: 1px solid #cccccc;
  // ↓水平居中
  text-align: center;
  padding: 8px;
  background-color: white;
  color: #666666;
  height: 45px;
}
.tdothers-home {
  // ↓将界面设置为无边框
  border: none;
  border-bottom: 1px solid #cccccc;
  text-align: center;
  padding: 12px;
}
td.UserHash-home {
  // ↓将界面设置为无边框
  border: none;
  border-bottom: 1px solid #cccccc;
  padding: 0 0 0 20px; // 上 右 下 左
  // ↓左对齐
  text-align: left;
  // ↓让Hash值换行
  word-break: break-all;
  width: 10%;
}
// ↓鼠标悬停时具有表格线
tr:hover {
  background-color: #f5f5f5;
}



.myform{
  height: 400px;
  overflow: auto;
  position: relative;
}
.barchart{
  margin-top: 20px;
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
