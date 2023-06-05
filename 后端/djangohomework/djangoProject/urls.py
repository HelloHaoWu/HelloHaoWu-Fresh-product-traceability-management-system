"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from ViewSet.views import Info4Customer, Info4Delivery, Info4Manager2, Info4Manager3, Info4Piedata, Info4Piedata_sub, Info4form1, Info4form2, Info4Linechart, Info4Linechartfixed, UpdateOrderStatus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Customer/', Info4Customer.as_view()),
    path('Delivery/', Info4Delivery.as_view()),
    path('Manager2/', Info4Manager2.as_view()),
    path('Manager3/', Info4Manager3.as_view()),
    path('Piedata/', Info4Piedata.as_view()),
    path('Piedata_sub/', Info4Piedata_sub.as_view()),
    path('form1/', Info4form1.as_view()),
    path('form2/', Info4form2.as_view()),
    path('Linechart/', Info4Linechartfixed.as_view()),
    path('updatestatus/', UpdateOrderStatus.as_view(), name='update_order_status'),
]
