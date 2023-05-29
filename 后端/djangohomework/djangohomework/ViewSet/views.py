from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import WareHouse, Supplier, Product, Customer, Order, Vehicle, OrderDetail, Dispatcher, Delivery, \
    ProductBatch


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
            targetID = request.GET['CID']  # 根据顾客编号, 返回信息
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
                'orderdetail__ProductBatch_ID__Supplier_ID',
                'orderdetail__ProductBatch_ID__Supplier_ID__Supplier_Name',
                'delivery__Dispatcher_ID',
                'delivery__Dispatcher_ID__Dispatcher_Tel',
                'orderdetail__ProductBatch_ID__WareHouse_ID',
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
                'orderdetail__ProductBatch_ID__Supplier_ID',
                'orderdetail__ProductBatch_ID__Supplier_ID__Supplier_Name',
                'delivery__Dispatcher_ID',
                'delivery__Dispatcher_ID__Dispatcher_Tel',
                'orderdetail__ProductBatch_ID__WareHouse_ID',
            )

        return Response(datalist)


class Info4Delivery(APIView):
    def get(self, request):
        # 获取数据集
        try:
            targetDelivery = request.GET['DID']  # 根据配送员编号, 返回数据
        except:
            targetDelivery = None

        if targetDelivery:
            datalist = Delivery.objects.filter(Delivery_ID=targetDelivery).values(
                'Dispatcher_ID',
                'Order_ID',
                'Latest_Delivery_Time',
                'Order_ID__orderdetail__ProductBatch_ID__ProductBatch_Expiration_Time',
                'Completion_Time',
                'Current_Status',
                'Vehicle_ID',
                'Current_Position',
                'Order_ID__Order_Destination',
            )
        else:
            datalist = Delivery.objects.filter().values(
                'Dispatcher_ID',
                'Order_ID',
                'Latest_Delivery_Time',
                'Order_ID__orderdetail__ProductBatch_ID__ProductBatch_Expiration_Time',
                'Completion_Time',
                'Current_Status',
                'Vehicle_ID',
                'Current_Position',
                'Order_ID__Order_Destination',
            )

        return Response(datalist)


class Info4Manager2(APIView):
    def get(self, request):
        # 获取数据集
        try:
            targetOrder = request.GET['OID']  # 根据订单编号, 返回数据
        except:
            targetOrder = None

        if targetOrder:
            datalist = Delivery.objects.filter(Order_ID=targetOrder).values(
                'Dispatcher_ID',
                'Order_ID',
                'Order_ID__Customer_ID',
                'Order_ID__Order_Destination',
                'Order_ID__orderdetail__ProductBatch_ID__ProductBatch_Expiration_Time',
                'Latest_Delivery_Time',
                'Completion_Time',
                'Vehicle_ID',
                'Current_Position',
                'Current_Status',
            )
        else:
            datalist = Delivery.objects.filter().values(
                'Dispatcher_ID',
                'Order_ID',
                'Order_ID__Customer_ID',
                'Order_ID__Order_Destination',
                'Order_ID__orderdetail__ProductBatch_ID__ProductBatch_Expiration_Time',
                'Latest_Delivery_Time',
                'Completion_Time',
                'Vehicle_ID',
                'Current_Position',
                'Current_Status',
            )

        return Response(datalist)


class Info4Manager3(APIView):
    def get(self, request):
        # 获取数据集
        try:
            targetPB = request.GET['PBID']  # 根据批次编号, 返回数据
        except:
            targetPB = None

        if targetPB:
            datalist = ProductBatch.objects.filter(ProductBatch_ID=targetPB).values(
                'ProductBatch_ID',
                'Product_ID',
                'WareHouse_ID',
                'Supplier_ID',
                'Product_ID__Product_Type',
                'ProductBatch_Supply_Amount',
                'ProductBatch_Warehousing_Time',
                'ProductBatch_Expiration_Time',
            )
        else:
            datalist = ProductBatch.objects.filter().values(
                'ProductBatch_ID',
                'Product_ID',
                'WareHouse_ID',
                'Supplier_ID',
                'Product_ID__Product_Type',
                'ProductBatch_Supply_Amount',
                'ProductBatch_Warehousing_Time',
                'ProductBatch_Expiration_Time',
            )

        return Response(datalist)

