from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# from .models import QNLogData
# from ViewSet.sers import QNLogDataSerializer

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
class Testdata(APIView):
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
        return Response([1322, 52199, 315292, 35122])