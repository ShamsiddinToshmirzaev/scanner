from rest_framework import serializers
from .models import Scan_Type, Result, Target, Scan


class ScanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan_Type
        fields = ('name', 'parent', 'command')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('xml', 'json')


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('target', 'type', 'user', 'ip')


class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = ('target', 'scan_type', 'start_date', 'finish_date', 'status', 'progress', 'command')
