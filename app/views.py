from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
class ProductCrud(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)
    def post(self,request,id):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'massage':'prodict id created'})
        return Response({'failed':'product is created'})

    def put(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'product is update'})
        return Response({'failed':'product is update'})
        

    def patch(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        PO.Pname=request.data['Pname']
        PO.save()
        return Response({'message':'patch successfully'})

    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'success':'product is deleted'})



