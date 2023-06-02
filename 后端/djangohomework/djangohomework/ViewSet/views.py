from django.shortcuts import render
from datetime import datetime
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
                'orderdetail__OrderDetail_ID',
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
                'orderdetail__OrderDetail_ID',
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

class Info4Piedata(APIView):
    def get(self,request):
        current_date = datetime.now()
        category_sums = {}
        datalist = Order.objects.filter(Order_Time__year=current_date.year,
                                        Order_Time__month=current_date.month - 1).values(  # 这里-1是因为没有6月的销售数据
            'orderdetail__Quantity',
            # 'Order_ID__OrderDetail_Quantity',
            'orderdetail__ProductBatch_ID__Product_ID__Product_Type'
                                        )
        for order in datalist:
            amount = order['orderdetail__Quantity']
            category = order['orderdetail__ProductBatch_ID__Product_ID__Product_Type']
            if category in category_sums:
                # 如果分类已经存在，将当前订单的金额加到对应分类的总和中
                category_sums[category] += amount
            else:
                # 如果分类不存在，将当前订单的金额作为该分类的初始总和
                category_sums[category] = amount
        '''data4pie = [
            {
                "种类": list(category_sums.keys())[0],
                "上月总销量": category_sums[list(category_sums.keys())[0]]
            },
            {
                "种类": list(category_sums.keys())[1],
                "上月总销量": category_sums[list(category_sums.keys())[1]]
            },
            {
                "种类": list(category_sums.keys())[2],
                "上月总销量": category_sums[list(category_sums.keys())[2]]
            },
            {
                "种类": list(category_sums.keys())[3],
                "上月总销量": category_sums[list(category_sums.keys())[3]]
            },
            {
                "种类": list(category_sums.keys())[4],
                "上月总销量": category_sums[list(category_sums.keys())[4]]
            }
        ]'''
        data4pie = []
        for k,v in category_sums.items():
            data4pie.append({"种类":k,"上月总销量":v})
        return Response(data4pie)
    
class Info4Piedata_sub(APIView):
    def get(self,request):
        datalist = WareHouse.objects.values(
            'WareHouse_ID',
            'productbatch__ProductBatch_Current_Inventory',
            'productbatch__Product_ID__Product_Type'
                                        )
        inventory = {}
        for line in datalist:
            warehouse = line['WareHouse_ID']
            quantity = line['productbatch__ProductBatch_Current_Inventory']
            ptype = line['productbatch__Product_ID__Product_Type']
            if quantity != None:
                if warehouse in inventory:
                    inventory[warehouse]['total'] += quantity
                    if ptype in inventory[warehouse]:
                        inventory[warehouse][ptype] += quantity
                    else:
                        inventory[warehouse][ptype] = quantity
                
                else:
                    inventory[warehouse] = {}
                    inventory[warehouse]['total'] = quantity
                    inventory[warehouse][ptype] = quantity
        # 根据"total"字段进行排序
        sorted_dict = sorted(inventory.items(), key=lambda x: x[1]["total"], reverse=True)
        # 选出前三个编号
        top_three = [item[0] for item in sorted_dict[:3]]
        result = {'piedata1':{},'piedata2':{},'piedata3':{}}
        for index in range(3):
            for k,v in inventory[top_three[index]].items():
                if k != 'total':
                    result['piedata'+str(index+1)][k] = v
        jsondict = {'piedata1':[],'piedata2':[],'piedata3':[]}
        for key,value in result.items():
            for k,v in value.items():
                typeline = {'value':v,'name':k}
                jsondict[key].append(typeline)
        return Response(jsondict)

class Info4form1(APIView):
    def get(self,request):
        datalist = WareHouse.objects.values(
            'WareHouse_ID',
            'productbatch__ProductBatch_Current_Inventory',
            'productbatch__Product_ID__Product_Type'
                                        )
        typedict = {}
        for line in datalist:
            ptype = line['productbatch__Product_ID__Product_Type']
            quantity = line['productbatch__ProductBatch_Current_Inventory']
            if quantity != None:
                if ptype in typedict:
                    typedict[ptype] += quantity
                else:
                    typedict[ptype] = quantity
        jsonlist = []
        for k,v in typedict.items():
            jsonlist.append({'生鲜种类':k,'库存总量':v})
        return Response(jsonlist)

class Info4form2(APIView):
    def get(self,request):
        '''datalist = OrderDetail.objects.values(
            'OrderDetail_ID',
            'Order_ID__Order_Time',
                                        )
        jsonlist = []
        for line in datalist:
            jsonlist.append({
                'orderdetail__OrderDetail_ID':line['OrderDetail_ID'],
                'Order_Time':line['Order_ID__Order_Time']
                })'''
        statusdic = {0:'未发货',1:'配送中',2:'已完成'}
        recent_orders = Order.objects.order_by('Order_Time').values(
            'Order_ID',
            'Customer_ID__Customer_Name',
            'Order_Time',
            'delivery__Current_Status'
            )[10:]
        jsonlist = []
        for line in recent_orders:
            jsonlist.insert(0,{
                "订单ID": line['Order_ID'],
                "订购者": line['Customer_ID__Customer_Name'],
                "下单时间": line['Order_Time'],
                "订单状态": statusdic[line['delivery__Current_Status']]
            })
        return Response(jsonlist)

class Info4Linechart(APIView):
    def get(self, request):
        current_date = datetime.now()
        category_sums = {}
        datalist = Order.objects.filter(Order_Time__year=current_date.year).values(  # 这里-1是因为没有6月的销售数据
            'Order_Time',
            'orderdetail__Quantity',
            'orderdetail__ProductBatch_ID__Product_ID__Product_Type'
        )
        sale_result = {}
        for line in datalist:
            month = int(str(line['Order_Time'])[5:7])
            quantity = line['orderdetail__Quantity']
            ptype = line['orderdetail__ProductBatch_ID__Product_ID__Product_Type']
            if ptype in sale_result:
                sale_result[ptype][((month - 1) // 3 + 1)] += quantity
            else:
                sale_result[ptype] = [0,0,0,0]
                sale_result[ptype][((month - 1) // 3 + 1)] += quantity
        print(sale_result)
        jsondict = {"legend":[],
                    "xAxis": ["a","b","c","d"],
                    }
        linecount = 1
        for k,v in sale_result.items():
            jsondict['legend'].append(k)
            jsondict['line'+str(linecount)] = {
                "name":k,
                "data":v
            }
            linecount += 1
        return Response(jsondict)

