from django.db import models

# class QNLogData(models.Model):
#     Lusername = models.CharField(max_length=60, verbose_name="App_username")
#     Lpassword = models.CharField(max_length=60, verbose_name="App_userpassword")
#
#     class Meta:
#         db_table = "Log_user"
#         verbose_name = "Table of users"
#         verbose_name_plural = verbose_name

# Create your models here. 
# Using MySql
class WareHouse(models.Model):
    pass

class Order(models.Model):
    pass

class Vehicle(models.Model):
    '''
    车辆信息
    车辆编号 Vehicle_id 主键
    仓库编号 WareHouse_id 车辆的归属仓库，外键为：仓库.仓库编号
    车辆型号 Vehicle_type
    '''
    Vehicle_id = models.IntegerField(primary_key=True, null=False)
    # 需要对被引用的外键首先定义，此处以WareHouse为名
    WareHouse_id = models.IntegerField(to=WareHouse,to_field="WareHouse_id", on_delete=models.CASCADE)
    # models中无法使用Varchar类型
    Vehicle_type = models.CharField(max_length=256,null=True,blank=True)

class Product(models.Model):
    '''
    产品信息
    产品编号 Product_id 主键
    产品名称 Product_name
    '''
    Product_id = models.IntegerField(primary_key=True,null=False)
    Product_name = models.CharField(max_length=256)

class OrderDetail(models.Model):
    '''
    订单明细
    订单明细编号 OrderDetail_id 主键
    产品编号 Product_id 订单中包含的产品的编号，外键为：产品.产品编号
    订单编号 Order_id 该订单明细属于哪个订单，外键为：订单.订单编号
    产品数量 Quantity Float类型，保留3位小数
    产品售价 SalePrice Float类型，保留两位小数
    '''
    OrderDetail_id = models.IntegerField(primary_key=True,null=False)
    Product_id = models.IntegerField(to=Product,to_field="Product_id", on_delete=models.CASCADE)
    Order_id = models.IntegerField(to=Order,to_field="Order_id", on_delete=models.CASCADE)
    Quantity = models.FloatField(default=0,decimal_places=3)
    SalePrice = models.FloatField(default=0,decimal_places=2)


