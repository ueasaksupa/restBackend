from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restapi.models import Portfolios
from restapi.serializers import PortfolioSerializer
# Create your views here.

@csrf_exempt
def portfolio_list(request):
    """
    List all Portfoios.
    """
    if request.method == 'GET':
        ports = Portfolios.objects.all()
        serializer = PortfolioSerializer(ports, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PortfolioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def portfolio_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        port = Portfolios.objects.get(pk=pk)
    except Portfolios.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PortfolioSerializer(port)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PortfolioSerializer(port, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        port.delete()
        return HttpResponse(status=204)