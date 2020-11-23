from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TypeSerializer
from .models import Scan_Type


class ScanTypeView(APIView):
    def get(self, request):
        types = Scan_Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response({"types": serializer.data})

    def post(self, request):
        type = request.data.get('type')

        # Create an article from the above data
        serializer = TypeSerializer(data=type)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Scan Type '{}' created successfully".format(article_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        type = get_object_or_404(Scan_Type.objects.all(), pk=pk)
        type.delete()
        return Response({"message": "Scan Type with id `{}` has been deleted.".format(pk)}, status=204)
