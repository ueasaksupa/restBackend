from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from restapi.models import Portfolios
from restapi.serializers import PortfolioSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.


class PortfolioList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PortfolioSerializer
    
    def get_queryset(self):
        queryset = Portfolios.objects.filter(owner=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Portfolios.objects.all()
    serializer_class = PortfolioSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer