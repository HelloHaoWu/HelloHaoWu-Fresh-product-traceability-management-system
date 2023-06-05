from django.db import models

class WareHouse(models.Model):
    '''
    仓库
    仓库编号 WareHouse_ID 主键
    仓库名称 WareHouse_Name
    仓库地址 WareHouse_Address
    '''
    WareHouse_ID = models.IntegerField(primary_key=True, null=False)
    WareHouse_Name = models.CharField(max_length=256)
    WareHouse_Address = models.CharField(max_length=256)

class Supplier(models.Model):
    '''
    供应商
    供应商编号 Supplier_ID 主键
    供应商名称 Supplier_Name
    '''
    Supplier_ID = models.IntegerField(primary_key=True, null=False)
    Supplier_Name = models.CharField(max_length=256)

class Product(models.Model):
    '''
    产品
    产品编号 Product_ID 主键
    产品名称 Product_Name
    产品类型 Product_Type
    '''
    Product_ID = models.IntegerField(primary_key=True, null=False)
    Product_Name = models.CharField(max_length=256)
    Product_Type = models.CharField(max_length=256)

class ProductBatch(models.Model):
    '''
    产品批次
    产品批次编号 ProductBatch_ID
    产品编号 Product_ID 外键 参照：产品.产品编号
    仓库编号 WareHouse_ID 外键 参照：仓库.仓库编号
    供应商编号 Supplier_ID 外键 参照：供应商.供应商编号
    批次当前库存 ProductBatch_Current_Inventory Float类型，保留3位小数【这边是和 订单明细 相符】
    批次生产时间 ProductBatch_Production_Time
    产地 ProductBatch_Production_Place
    过期时间 ProductBatch_Expiration_Time
    入库时间 ProductBatch_Warehousing_Time
    供应时间 ProductBatch_Supply_Time
    供应量 ProductBatch_Supply_Amount Float类型，保留3位小数【这边是和 订单明细 相符】
    供应地址 ProductBatch_Supply_Address
    '''
    ProductBatch_ID = models.IntegerField(primary_key=True, null=False)
    Product_ID = models.ForeignKey(to=Product, to_field="Product_ID", on_delete=models.CASCADE)
    WareHouse_ID = models.ForeignKey(to=WareHouse, to_field="WareHouse_ID", on_delete=models.CASCADE)
    Supplier_ID = models.ForeignKey(to=Supplier, to_field="Supplier_ID", on_delete=models.CASCADE)
    ProductBatch_Current_Inventory = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    ProductBatch_Production_Time = models.DateTimeField(null=True, blank=True)
    ProductBatch_Production_Place = models.CharField(max_length=256)
    ProductBatch_Expiration_Time = models.DateTimeField(null=True, blank=True)
    ProductBatch_Warehousing_Time = models.DateTimeField(null=True, blank=True)
    ProductBatch_Supply_Time = models.DateTimeField(null=True, blank=True)
    ProductBatch_Supply_Amount = models.DecimalField(default=0, decimal_places=3, max_digits=10)  # Decimalfield必须指定max_digits
    ProductBatch_Supply_Address = models.CharField(max_length=256)

class Customer(models.Model):
    '''
    客户信息
    客户编号 Customer_ID
    客户姓名 Customer_Name
    客户性别 Customer_Sex 1代表"男",0代表"女"
    客户年龄 Customer_Age
    联系方式 Customer_Tel
    客户类型 Customer_Type
    '''
    Customer_ID = models.IntegerField(primary_key=True, null=False)
    Customer_Name = models.CharField(max_length=256)
    Customer_Sex = models.IntegerField(choices=((1, "男"), (0, "女")), null=False)
    Customer_Age = models.IntegerField(default=0)
    Customer_Tel = models.CharField(max_length=256, null=True, blank=True)
    Customer_Type = models.CharField(max_length=256)

class Order(models.Model):
    '''
    订单信息
    订单编号 Order_ID 主键
    订单时间 Order_Time 自动为添加数据的时间
    客户编号 Customer_ID 外键 参照为: 客户, 客户编号
    收货地址 Order_Destination
    配送编号 [取消]
    '''
    Order_ID = models.IntegerField(primary_key=True, null=False)
    Order_Time = models.DateTimeField(auto_now_add=True)
    Customer_ID = models.ForeignKey(to=Customer, to_field="Customer_ID", on_delete=models.CASCADE)
    Order_Destination = models.CharField(max_length=256)

class Vehicle(models.Model):
    '''
    车辆信息
    车辆编号 Vehicle_id 主键
    仓库编号 WareHouse_id 外键 车辆的归属仓库, 参照为: 仓库·仓库编号
    车辆编号 Vehicle_type
    '''
    Vehicle_ID = models.IntegerField(primary_key=True, null=False)
    # 需要对被引用的外键首先定义, 此处以WareHouse为名
    WareHouse_ID = models.ForeignKey(to=WareHouse, to_field="WareHouse_ID", on_delete=models.CASCADE)
    # on_delete=models.CASCADE 的作用是当关联对象被删除时, 与之相关的对象也会被删除
    # models无法使用Varchar类型
    Vehicle_Type = models.CharField(max_length=256, null=True, blank=True)

class OrderDetail(models.Model):
    '''
    订单明细
    订单明细编号 OrderDetail_id 主键
    产品编号 Product_id 外键 订单中包含的产品的编号, 参照为: 产品·产品编号
    订单编号 Order_id 外键 该订单明细属于哪个订单, 参照为: 订单·订单编号
    产品数量 Quantity Float类型, 保留3位小数
    产品售价 SalePrice Float类型, 保留2位小数
    '''
    OrderDetail_ID = models.IntegerField(primary_key=True, null=False)
    ProductBatch_ID = models.ForeignKey(to=ProductBatch, to_field="ProductBatch_ID", on_delete=models.CASCADE)
    Order_ID = models.ForeignKey(to=Order, to_field="Order_ID", on_delete=models.CASCADE)
    Quantity = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    SalePrice = models.DecimalField(default=0, decimal_places=2, max_digits=10)

class Dispatcher(models.Model):
    '''
    配送人员
    编号 Dispatcher_ID
    姓名 Dispatcher_Name
    性别 Dispatcher_Sex
    年龄 Dispatcher_Age
    联系方式 Dispatcher_Tel
    所属仓库 WareHouse_ID 外键，参照：仓库.仓库编号
    '''
    Dispatcher_ID = models.IntegerField(primary_key=True, null=False)
    Dispatcher_Name = models.CharField(max_length=256)
    Dispatcher_Sex = models.IntegerField(choices=((1, "男"), (0, "女")), null=False)
    Dispatcher_Age = models.IntegerField(default=0)
    Dispatcher_Tel = models.CharField(max_length=256, null=True, blank=True)
    WareHouse_ID = models.ForeignKey(to=WareHouse, to_field="WareHouse_ID", on_delete=models.CASCADE)

class Delivery(models.Model):
    '''
    配送信息
    配送编号 Delivery_ID 主键
    订单编号 Order_ID 外键 参照：订单.订单编号
    配送员编号 Dispatcher_ID 外键 参照：配送人员.配送人员编号
    车辆编号 Vehicle_ID 外键 参照：车辆.车辆编号
    最晚送达时间 Latert_Delivery_Time 【通过产品生产日期与保质期确定】
    当前状态 Current_Status 【从前端获取】
    当前位置 Current_Position 【不知如何插入】
    完成配送时间 Completion_Time 完成订单时，记录时间
    '''
    Delivery_ID = models.IntegerField(primary_key=True, null=False)
    Order_ID = models.ForeignKey(to=Order, to_field="Order_ID", on_delete=models.CASCADE)
    Dispatcher_ID = models.ForeignKey(to=Dispatcher, to_field="Dispatcher_ID", on_delete=models.CASCADE)
    Vehicle_ID = models.ForeignKey(to=Vehicle, to_field="Vehicle_ID", on_delete=models.CASCADE)
    Latest_Delivery_Time = models.DateField(null=True, blank=True)
    Current_Status = models.IntegerField(choices=((0, "即将配送"), (1, "正在配送中"), (2, "已送达")),default=0)
    Current_Position = models.CharField(max_length=256)
    Completion_Time = models.DateTimeField(null=True, blank=True)