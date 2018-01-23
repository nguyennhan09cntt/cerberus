from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from cerberus.api.serializers import ClassifySerializer
from lib.classifier.rent_classifier import CerberusRentClassifier

# Create your views here.

class RentClassify(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
      data = request.GET.get('input', '')
      classify_rent = CerberusRentClassifier()
      result = classify_rent.classify(data)
      advertisementClassify = {"status": 10, "message": result, "created": ""}
      results= ClassifySerializer(advertisementClassify, many=False).data
      return Response(results)

    def post(self, request, format=None):
      return  Response({'message':'post'})