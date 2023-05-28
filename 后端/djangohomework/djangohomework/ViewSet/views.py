from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import WareHouse, Supplier, Product, Customer, Order, Vehicle, OrderDetail, Dispatcher, Delivery, ProductBatch

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
    
class Info4Customer(APIView):
    def get(self, request):
        # 获取数据集
        try:
            targetID = request.GET['CID']
        except:
            targetID = None
        # 如何从前端获得用户ID? 通过如上方法↑

        if targetID:
            datalist = Order.objects.filter(Customer_ID=targetID).values(
                    'Order_Time',
                    'Customer_ID__Customer_Name',
                    'Order_Destination',
                    'orderdetail__ProductBatch_ID__Product_ID__Product_Type',
                    'Customer_ID__Customer_Sex',
                    'Customer_ID__Customer_Tel',
                    'orderdetail__OrderDetail_ID'
                )

        else:
            datalist = Order.objects.filter().values(
                'Order_Time',
                'Customer_ID__Customer_Name',
                'Order_Destination',
                'orderdetail__ProductBatch_ID__Product_ID__Product_Type',
                'Customer_ID__Customer_Sex',
                'Customer_ID__Customer_Tel',
                'orderdetail__OrderDetail_ID'
            )

        return Response(datalist)
    
# class Info4Order(APIView):
#     def get(self, request):
#         TargetID = 123456
#         datalist = Order.objects.filter(Order_ID=TargetID).values_list(
#             'OrderDetail__Product_ProductBatch__Supplier__Supplier_ID',
#             'OrderDetail__Product_ProductBatch__Supplier__Supplier_Name',
#             'Delivery__Dispatcher__Dispatcher_ID',
#             'Delivery__Dispatcher__Dispatcher_Tel',
#             'Delivery__Dispatcher__WareHouse__WareHouse_Name',
#         )
#         ser = OrderDetailSerializer(instance=datalist,many = False)
#         data = ser.data
#         return Response(data)
#
# class Info4Delivery(APIView):
#     def get(self, request):
#         TargetDelivery = request.GET['DID']   # 获取数据集
#         if not TargetDelivery:
#             return Response('请在发送时附加配送单ID作为参数.')
#         datalist = Delivery.objects.filter(Delivery_ID=TargetDelivery).values_list(
#             'Dispatcher_ID',
#             'Order_ID',
#             'Latest_Delivery_Time',
#             'Current_Status',
#             'Vehicle_ID',
#             'Current_Position',  # 'buttonText'是什么?这个我没太懂就没实现
#         )
#         ser = OrderDetailSerializer(instance=datalist, many=False)
#         data = ser.data
#         return Response(data)