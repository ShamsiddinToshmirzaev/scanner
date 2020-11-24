from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ScanTypeSerializer
from .models import Scan_Type
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import permissions, serializers


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/type-list/',
        'Detail View': '/type-detail/<str:pk>/',
        'Create': '/type-create/',
        'Update': '/type-update/<str:pk>/',
        'Delete': '/type-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def typeList(request):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    types = Scan_Type.objects.all()
    serializer = ScanTypeSerializer(types, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def typeDetail(request, pk):
    types = Scan_Type.objects.get(id=pk)
    serializer = ScanTypeSerializer(types, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def typeCreate(request):
    serializer = ScanTypeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def typeUpdate(request, pk):
    type = Scan_Type.objects.get(id=pk)
    serializer = ScanTypeSerializer(instance=type, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def typeDelete(request, pk):
    type = Scan_Type.objects.get(id=pk)
    type.delete()
    return Response("Type Deleted Successfully")
