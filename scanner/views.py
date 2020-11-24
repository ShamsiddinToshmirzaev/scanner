from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ScanTypeSerializer, ResultSerializer
from .models import Scan_Type, Result


# for Scan Type Model
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


# for Result Model
@api_view(['GET'])
def resultList(request):
    results = Result.objects.all()
    serializer = ResultSerializer(results, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def resultDetail(request, pk):
    results = Result.objects.get(id=pk)
    serializer = ResultSerializer(results, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def resultCreate(request):
    serializer = ResultSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, 201)


@api_view(['POST'])
def resultUpdate(request, pk):
    result = Result.objects.get(id=pk)
    serializer = ResultSerializer(instance=result, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def resultDelete(request, pk):
    result = Result.objects.get(id=pk)
    result.delete()
    return Response("Result Deleted Successfully")
