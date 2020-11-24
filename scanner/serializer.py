from rest_framework import serializers
from .models import Scan_Type


class ScanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan_Type
        fields = ('name', 'parent', 'command')
