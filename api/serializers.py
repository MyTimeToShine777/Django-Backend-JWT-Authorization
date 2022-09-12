
from rest_framework import serializers
from base.models import ApiData


class ApiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiData
        fields = '__all__'
