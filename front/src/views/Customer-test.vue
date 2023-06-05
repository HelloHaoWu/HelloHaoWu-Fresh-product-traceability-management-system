<template>
  <div class="customerpage">
    <div class="head">
      <div class="title"><strong>客户订单列表</strong></div>
      <div class="card-body" v-if="JudgeUserType(this.user)">
        <!-- 添加用户 -->
        <div class="form-inline">
          <div class="input-group mb-2 mr-sm-2">
            <div class="input-group-prepared">
              <div class="input-group-text">客户搜索:</div>
            </div>
          </div>
          <!-- 文本输入框 -->
          <input @keyup.esc="searchValue=''" v-model="searchValue" type="text" class="form-control" />
        </div>
      </div>
    </div>
    <el-card class="customerCard">
      <el-scrollbar class="blockdetail_rightpart">
        <el-main style="padding: 0;">
          <!-- ↓这个不用改css样式, 随着行数增加会自动和选页数部分接触到 -->
          <div class="like_table">
            <span class="like-th"></span>
            <span class="like_tr" v-for="(item, index) in orders" :key="item.orderdetail__OrderDetail_ID">
              <div class="short_data">
                <div class="tr_OrderId">
                  <div>详情号：{{index + 1 + (this.current_page-1)*(this.pageData.limit)}}</div>
                </div>
                <div class="tr_CustName">
                  <div>顾客名称：{{ item.Customer_ID__Customer_Name }}</div>
                </div>
                <div class="tr_ProductName">
                  <div>订购产品：{{ item.orderdetail__ProductBatch_ID__Product_ID__Product_Name}}</div>
                </div>
                <div class="tr_OrderTime">
                  <div>订单时间：{{ replace(item.Order_Time)}}</div>
                </div>
                <div class="tr_OrderStatus">
                  <el-tag :type="JudgeColor_FromNum(item.delivery__Current_Status)">{{ JudgeText_FromNum(item.delivery__Current_Status) }}</el-tag>
                </div>
                <div class="show_details">
                  <ion-icon id="collapselink" name="chevron-down-outline" class="detail_click" v-on:click="Rotate_and_show(index)"></ion-icon>
                </div>
              </div>
              <div class="detail_data_incustomer">
                <div class="side_table">
                  <div class="left_colname">
                    <div class="type_colname">产品种类：</div>
                    <div class="supplier_colname">供应商：</div>
                    <div class="Ori_warehouse">始发仓库：</div>
                  </div>
                  <div class="left_detail">
                    <div class="pro_type">{{ item.orderdetail__ProductBatch_ID__Product_ID__Product_Type }}</div>
                    <div class="pro_supplier">{{ item.orderdetail__ProductBatch_ID__Supplier_ID__Supplier_Name }}</div>
                    <div class="pro_type">{{ item.orderdetail__ProductBatch_ID__WareHouse_ID__WareHouse_Name }}</div>
                  </div>
                  <div class="middle_colname">
                    <div class="dest_colname">目的地：</div>
                    <div class="cur_colname">当前位置：</div>
                    <div class="phone_colname">配送员电话：</div>
                  </div>
                  <div class="middle_detail">
                    <div class="pro_dest">{{ item.Order_Destination }}</div>
                    <div class="pro_cur">{{ item.delivery__Current_Position }}</div>
                    <div class="pro_phone">{{ item.delivery__Dispatcher_ID__Dispatcher_Tel }}</div>
                  </div>
                  <div class="right_colname">
                    <div class="dest_colname">生产时间：</div>
                    <div class="cur_colname">过期时间：</div>
                  </div>
                  <div class="right_detail">
                    <div class="pro_dest">{{ replace(item.orderdetail__ProductBatch_ID__ProductBatch_Production_Time) }}</div>
                    <div class="pro_cur">{{ replace(item.orderdetail__ProductBatch_ID__ProductBatch_Expiration_Time) }}</div>
                  </div>
                </div>
              </div>
            </span>
          </div>
        </el-main>
        <el-pagination layout="prev, pager, next" :current-page=this.current_page :total="total" :page-size=16 @current-change="handlePage"/>
      </el-scrollbar>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";
import {useUserStore} from "./login.vue";
// import * as echarts from "echarts";
// import elementResizeDetectorMaker from 'element-resize-detector'
// const erd = elementResizeDetectorMaker()

export default {
  name: "AppBlockDetail",
  data() {
    const store = useUserStore();
    return {
      user: store.user,
      userid: store.id,
      total: 0,
      customerdetail: [],
      orders: [],
      current_page: 1, // 当前页码
      pageData: { // 展示页用
        page: 1,
        limit: 16
      },
      searchValue: '',
      newValue_search: '',
    }
  },
  created() {
    this.Loadcustomerdata()
  },
  watch: {
    searchValue(newValue) {
      // console.log(newValue)
      axios
          .get(`http://43.143.167.222:8020/Customer/?CNAME=${newValue}`)
          .then(res => {
            console.log(res.data)
            // this.list = res.data
            // ↓测试用, 真实使用时请结合后端反馈信息进行操作
            if (res.data === false) {
              alert('查询结果为空，即将清空搜索栏，请尝试再次查询。')
              this.loadData()
              this.searchValue = ''
            }
                // // ↓当差不到时要执行的动作还没写(连接django后端用)
                // if (res.data == '访问结果为空.') {
                //   alert('查询结果为空，请清空搜索栏后再次尝试查询.')
                // }
            // 只显示前20个, 查询结果不够20个退出循环 → 管用!
            else {
              this.pageData.page = 1
              this.orders = []
              this.current_page = 1
              for(let i=(this.pageData.page-1)*this.pageData.limit, j=0; j < this.pageData.limit; i++) {
                this.orders[j] = res.data[i];
                j++;
                if (i === res.data.length - 1) {
                  break
                }
              }
              this.newValue_search = newValue
              this.total = res.data.length || 0
            }
          })
    }
  },
  methods: {
    replace(str) {
      return str.replace("T", " ").replace("Z", " ");
    },
    // 点击改变样式, 同时显示详情页
    Rotate_and_show(index) {
      const linkCollapse = document.getElementsByClassName('detail_click')
      const form_blockdetail = document.getElementsByClassName('detail_data_incustomer')
      linkCollapse[index].classList.toggle('rotate')

      var num = 1 * 51 + 45 + 5
      if (form_blockdetail[index].style.height === num.toString() + 'px'){
        form_blockdetail[index].style.height = '0px'
      }
      else {
        form_blockdetail[index].style.height = num.toString() + 'px'
      }
      form_blockdetail[index].classList.toggle('showCollapse')
    },
    // 判断并返回订单状态
    // 1.返回标签色
    JudgeColor_FromNum(status) { // 渲染状态色
      if (status === 0) {
        return 'warning'
      } else if (status === 1) {
        return ''
      } else {
        return 'success'
      }
    },
    // 2.返回标签内容
    JudgeText_FromNum(status) { // 渲染状态色
      if (status === 0) {
        return '未配送'
      } else if (status === 1) {
        return '配送中'
      } else {
        return '已配送'
      }
    },
    // 获取"trans"信息
    Loadcustomerdata() {
      if (this.user === 'manager') {
        axios
            .get(`http://43.143.167.222:8020/Customer/`)
            .then(res => {
              console.log('你是经理', res.data)
              this.customerdetail = res.data
              var customerdetail = this.customerdetail
              // 分页
              this.total = customerdetail.length || 0
              console.log(this.total)
              this.orders = []
              for(let i=(this.pageData.page-1)*this.pageData.limit, j=0; j < this.pageData.limit; i++) {
                this.orders[j] = customerdetail[i];
                j++;
                if (i === customerdetail.length - 1) {
                  break
                }
              }
            })
      } else {
        axios
            .get(`http://43.143.167.222:8020/Customer/?CID=${this.userid}`)
            .then(res => {
              console.log('你是顾客', res.data)
              this.customerdetail = res.data
              var customerdetail = this.customerdetail
              // 分页
              this.total = customerdetail.length || 0
              console.log(this.total)
              this.orders = []
              for(let i=(this.pageData.page-1)*this.pageData.limit, j=0; j < this.pageData.limit; i++) {
                this.orders[j] = customerdetail[i];
                j++;
                if (i === customerdetail.length - 1) {
                  break
                }
              }
            })
      }
    },
    // 页码跳转用
    handlePage(val) {
      console.log(val)
      this.pageData.page = val
      this.current_page = val
      if (this.searchValue === ''){
        this.Loadcustomerdata()
      }
      else {
        this.loadcustomerdataSub()
      }
    },
    // 判断是否显示搜索栏
    JudgeUserType(usertype) {
      return usertype === 'manager';
    },
    // 搜索栏的值变化
    loadcustomerdataSub() {
      axios
          .get(`http://43.143.167.222:8020/Customer/?CNAME=${this.newValue_search}`)
          .then(res => {
            console.log(res.data)
            // this.list = res.data

            // 只显示前20个, 查询结果不够20个退出循环 → 管用!
            this.orders = []
            for(let i=(this.pageData.page-1)*this.pageData.limit, j=0; j < this.pageData.limit; i++) {
              this.orders[j] = res.data[i];
              j++;
              if (i === res.data.length - 1) {
                break
              }
            }
            this.total = res.data.length || 0
          })
    }
  }
}
</script>

<style lang="less">
.customerpage {
  margin-left: 14vh;
  margin-right: 2vh;
  margin-top: 4vh;
  .head {
    display: flex;
    justify-content: space-between;
    width: 100%;
    .title {
      display: flex;
      justify-content: center; /* 水平居中 */
      align-items: center; /* 垂直居中 */
      font-size: 20px;
    }
    .card-body {
      .form-inline {
        display: flex;
        width: 100%;
        .input-group {
          font-weight: normal;
          font-size: 20px;
        }
        .form-control {
          margin-left: 15px;
          width: 500px;
        }
      }
    }
    margin-left: -80px;
    margin-bottom: -40px;
  }
  .customerCard {
    color: #111111;
    width: 100%;
    height: 100%;
    margin: 70px 30px 20px -80px; // 上 右 下 左
    .like_table {
      display: flex;
      // ↓这行是最重要的, 这行使得"flex"的内容换行显示
      flex-direction: column; //按列显示
      // ↓这行啥意思没弄懂
      justify-content: space-around;
      // ↓这行啥意思也没弄懂
      box-sizing: border-box;
      width: 100%;
      // ↓↓这两行让这个类表容器有上下虚线底边
      border-top: 1px solid var(--el-border-color);
      //border-bottom: 1px solid var(--el-border-color);
      .like_tr {
        // ↓让每行具有下底边
        border-bottom: 1px solid var(--el-border-color);
        .short_data {
          display: flex;
          flex-direction: row;
          //border-bottom: 1px solid var(--el-border-color);
          width: 100%;
          //justify-content: space-between;
          align-items: flex-start;
          box-sizing: border-box;
          font-size: 0.85rem;
          .tr_OrderId {
            width: 20%;
            margin: 10px 16px 10px 8px; // 上 右 下 左
            font-size: 15px;
          }
          .tr_CustName {
            width: 20%;
            margin: 10px 0 10px 0;
            font-size: 15px;
          }
          .tr_ProductName {
            width: 20%;
            margin: 10px 0 10px 0;
            font-size: 15px;
          }
          .tr_OrderTime {
            text-align: right;
            width: 17%;
            margin: 10px 16px 10px 0;
            font-size: 15px;
          }
          .tr_OrderStatus {
            margin: 10px 0 10px 0;
            display: flex;
            justify-content: center;
            align-items: center;
          }
          .show_details {
            margin: 10px 16px 10px 0;
            text-align: left;
            width: 15%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            .detail_click {
              cursor:pointer;
              transition: .5s;
            }
          }
        }
        .detail_data_incustomer {
          display: flex;
          flex-direction: row; //按列显示
          //display: none;
          height: 0;
          //border-top: 1px solid var(--el-border-color);
          transition: .5s;
          /*溢出隐藏, 非常重要!!!*/
          overflow: hidden;
          .side_table {
            width: 100%;
            border-top: 1px solid var(--el-border-color);
            margin: 0 8px 0 8px; // 上 右 下 左
            padding: 10px 0 10px 0;
            display: flex;
            flex-direction: row;
            .left_colname {
              flex-direction: column;
              justify-content: space-between;
              width: 8%;
            }
            .left_detail {
              width: 21%;
            }
            .middle_colname {
               width: 8%;
            }
            .middle_detail {
              width: 27%;
            }
            .right_colname {
              width: 8%;
            }
            .right_detail {
              width: 28%;
            }
          }
        }
        // ↓得放到同一层CSS中才生效
        .showCollapse {
          //display: block;
          height: 100px;
          //border-top: 1px solid var(--el-border-color);
        }
        .rotate {
          transform: rotate(180deg);
        }
      }
    }
  }
}
</style>