from rest_framework import serializers
from .models import Scan_Type, Result


class ScanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan_Type
        fields = ('name', 'parent', 'command')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('xml', 'json')
