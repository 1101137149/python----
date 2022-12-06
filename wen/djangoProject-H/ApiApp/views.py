from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import FoodSerializer
from .models import Food

class  FoodViewSet(viewsets.ModelViewSet):
    #查詢所有產品 按name排序
    queryset = Food.objects.all().order_by('id')
    #指定 序列化 類別
    serializer_class = FoodSerializer