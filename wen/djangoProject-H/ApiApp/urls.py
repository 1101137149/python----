#設定網址路由器
from django.urls import path, include
from rest_framework import routers
from . import views

#router 路由器(總機小姐)
router = routers.DefaultRouter()

#配對path 與 view(分機小組)
#http://127.0.0.1:8000/product
router.register(r'Food', views. FoodViewSet)

#設定 總機小姐 路由(2組)
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/api/
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]