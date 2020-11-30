import re

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ScanTypeSerializer, ResultSerializer, TargetSerializer, ScanSerializer
from .models import Scan_Type, Result, Target, Scan
import socket
from urllib.parse import urlparse


# for Scan Type Model
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/type-list/',
#         'Detail View': '/type-detail/<str:pk>/',
#         'Create': '/type-create/',
#         'Update': '/type-update/<str:pk>/',
#         'Delete': '/type-delete/<str:pk>/',
#     }
#     return Response(api_urls)


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


# for Target Model

@api_view(['GET'])
def targetList(request):
    targets = Target.objects.all()
    serializer = TargetSerializer(targets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def targetDetail(request, pk):
    targets = Target.objects.get(id=pk)
    serializer = TargetSerializer(targets, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def targetCreate(request):
    pattern = "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"
    pattern2 = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
    if pattern:
        # prog = re.compile(pattern)
        target = request.POST.get('target')
        # target = prog.match(target1)
        ip = socket.gethostbyname(urlparse(target).netloc)
        type = "url"

    elif pattern2:
        # prog = re.compile(pattern2)
        target = request.POST.get('target')
        # target = prog.match(target2)
        # return HttpResponse(target)
        ip = socket.gethostbyname(target)
        return HttpResponse(ip)
        type = "hostname"

    else:
        return False
    # return HttpResponse(ip)

    serializer = TargetSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user, ip=ip, type=type)
    return Response(serializer.data, 201)


@api_view(['POST'])
def targetUpdate(request, pk):
    target = request.POST.get('target')
    ip = socket.gethostbyname(target)
    targets = Target.objects.get(id=pk)
    serializer = TargetSerializer(instance=targets, data=request.data)

    if serializer.is_valid():
        serializer.save(ip=ip)
    return Response(serializer.data)


@api_view(['DELETE'])
def targetDelete(request, pk):
    target = Target.objects.get(id=pk)
    target.delete()
    return Response("Target Deleted Successfully")


#  for Scan Model

@api_view(['GET'])
def scanList(request):
    scans = Scan.objects.all()
    serializer = ScanSerializer(scans, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def scanDetail(request, pk):
    scans = Scan.objects.get(id=pk)
    serializer = ScanSerializer(scans, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def scanCreate(request):
    target = Target.objects.all().first()
    scan_type = Scan_Type.objects.all().first()
    # return HttpResponse(scan_type)
    serializer = ScanSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(target=target, scan_type=scan_type)
    return Response(serializer.data, 201)
