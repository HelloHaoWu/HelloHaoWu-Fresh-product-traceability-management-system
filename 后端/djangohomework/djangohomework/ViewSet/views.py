from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import WareHouse,Supplier,Product,Customer,Order,Vehicle,OrderDetail,Dispatcher,Delivery,ProductBatch
from .sers import CustomerInfoSerializer,OrderDetailSerializer,DeliveryInfoSerializer

# Create your views here.
# class StudentViewSet(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer

# class QNLogDataView(APIView):
#     def get(self, request):
#         username = request.GET['username']
#         password = request.GET['password']
#         if not (username and password):
#             return Response('用户名或密码不能为空.')
#
#         # 查询用户是否存在
#         try:
#             userdata = QNLogData.objects.get(Lusername=username, Lpassword=password)
#             serializer = QNLogDataSerializer(instance=userdata, many=False)
#             return Response(serializer)
#         except QNLogData.DoesNotExist:
#             return Response('用户不存在于数据库中.')

# !!!拿各范围违法节点数(这个以后得重新写, 这个不能这么写, 以后得根据数据库进行数据统计)
'''class Testdata(APIView):
    def get(self, request):
        this = {
            "code": 202,
            "option0": {
                "title": {
                    "text": "my echarts"
                },
                "tooltip": {},
                "legend": {
                    "data": ["肉类", "蔬菜", "蛋类"]
                },
                "xAxis": {
                    "data": ["A", "B", "C", "D", "E"]
                },
                "yAxis": {},
                "series": [
                    {
                        "name": "肉类",
                        "data": [10, 22, 28, 43, 49],
                        "type": "line",
                        "stack": "x",
                        "itemStyle": {"color": "red"},
                        "emphasis": {
                            "itemStyle": {
                                "color": "red"
                            }
                        }
                    },
                    {
                        "name": "蔬菜",
                        "data": [5, 4, 3, 5, 10],
                        "type": "line",
                        "stack": "x",
                        "itemStyle": {"color": "green"},
                        "emphasis": {
                            "itemStyle": {
                                "color": "green"
                            }
                        }
                    },
                    {
                        "name": "蛋类",
                        "data": [5, 4, 3, 5, 10],
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
            },
            "option1": {
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
            }, "option2": { "tooltip": {}, "series": [ { "type": "pie", "data": [ { "value": 335, "name": "直接访问" }, { "value": 234, "name": "联盟广告" }, { "value": 1548, "name": "搜索引擎" } ] } ] }, "option3": { "tooltip": {}, "series": [ { "type": "pie", "data": [ { "value": 335, "name": "直接访问" }, { "value": 234, "name": "联盟广告" }, { "value": 1548, "name": "搜索引擎" } ] } ] } }
        return Response(this)

# !!!拿各季度违法节点总共的交易数(这个以后得重新写, 这个不能这么写, 以后得根据数据库进行数据统计)
class EchartsData(APIView):
    def get(self, request):
        return Response([0, 4, 81, 196, 235, 73, 193, 385, 388, 1354, 3336, 3564, 3637, 2790, 2028, 1849, 1880, 3136, 714, 97])

# !!!拿各统计数据(这个以后得重新写, 这个不能这么写, 以后得根据数据库进行数据统计)
class Datahome(APIView):
    def get(self, request):
        return Response([1322, 52199, 315292, 35122])'''
    
class Info4Customer(APIView):
    def get(self, request):
        # 获取数据集
        targetID = 123456  #如何从前端获得用户ID？
        datalist = Order.objects.filter(Customer__Customer_ID=targetID).values_list(
            'Order_Time','Customer__Customer_Name','Order_Destination','OrderDetail__Product__Product_Type','Customer__Customer_Sex','Customer__Customer_Tel','Order_ID'
            )
        # 实例化序列化器，得到序列化器对象
        ser = CustomerInfoSerializer(instance=datalist, many=True)
        # 调用序列化器对象的data属性方法获取转换后的数据
        data = ser.data
        # 响应数据
        return Response(data)
    
class Info4Order(APIView):
    def get(self,request):
        TargetID = 123456
        datalist = Order.objects.filter(Order_ID=TargetID).values_list(
            'OrderDetail__Product_ProductBatch__Supplier__Supplier_ID',
            'OrderDetail__Product_ProductBatch__Supplier__Supplier_Name',
            'Delivery__Dispatcher__Dispatcher_ID',
            'Delivery__Dispatcher__Dispatcher_Tel',
            'Delivery__Dispatcher__WareHouse__WareHouse_Name',
        )
        ser = OrderDetailSerializer(instance=datalist,many = False)
        data = ser.data
        return Response(data)
    
class Info4Delivery(APIView):
    def get(self,request):
        TargetDispatcher = 123456
        datalist = Delivery.objects.filter(Dispatcher__Dispatcher_ID=TargetDispatcher).values_list(
            'Order_ID',
            'Latest_Delivery_Time',
            'Current_Status',
            'Vehicle_ID',
            'Current_Position',
        )
        ser = OrderDetailSerializer(instance=datalist,many = False)
        data = ser.data
        return Response(data)