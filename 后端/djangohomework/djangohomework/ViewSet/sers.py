from rest_framework import serializers
# from ViewSet.models import QNLogData

# 创建序列化器类, 会在视图(views)中被调用

# class QNLogDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QNLogData
#         fields = "__all__"

class CustomerInfoSerializer(serializers.Serializer):
    OrderTime= serializers.DateTimeField()
    CustomerName = serializers.CharField()
    Address = serializers.CharField()
    ProductType = serializers.CharField()
    Sex = serializers.IntegerField()
    Tel = serializers.IntegerField()
    OrderID = serializers.IntegerField()

class OrderDetailSerializer(serializers.Serializer):
    SupplierName = serializers.CharField()
    SupplierID = serializers.IntegerField()
    DispatcherID = serializers.IntegerField()
    DispatcherTel = serializers.IntegerField()
    WareHouse = serializers.CharField()

class DeliveryInfoSerializer(serializers.Serializer):
    DispatcherID = serializers.IntegerField()
    OrderID = serializers.IntegerField()
    LatestTime = serializers.DateTimeField()
    OrderStatus = serializers.IntegerField()
    VehicleID = serializers.IntegerField()
    CurrentLocation = serializers.CharField()
    




