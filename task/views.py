from django.shortcuts import render
from .models import Restaurant
from .serializer import RestauSerialeizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers


# Create your views here.


@api_view(['GET','POST','DELETE'])

def listview(request):
   if request.method == "GET":
      objList=Restaurant.objects.all()
      serializer=RestauSerialeizer(objList,many=True)
      return Response(serializer.data)
   elif request.method == "POST":
      data=request.data
      serializer=RestauSerialeizer(data=data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
   else:
      data=request.data
      obj=Restaurant.objects.get(id=data['id'])
      obj.delete()
      return Response("deleted")