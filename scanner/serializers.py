from rest_framework import serializers
from .models import Scan_Type


class TypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    parent = serializers.CharField()
    command = serializers.CharField()

    def create(self, validated_data):
        return Scan_Type.objects.create(**validated_data)
