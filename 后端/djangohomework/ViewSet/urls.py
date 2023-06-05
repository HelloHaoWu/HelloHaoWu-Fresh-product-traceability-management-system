from rest_framework.routers import DefaultRouter
from . import views

# 路由列表
urlpatterns = []

router = DefaultRouter()  # 可以处理视图的路由器

# router.register('tabledata', views.TabledataViewSet)  # 向路由中注册视图
# router.register('echartslabelnum', views.EchartsLabelNumViewSet)
#
# urlpatterns += router.urls

