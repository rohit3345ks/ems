from rest_framework import serializers
from .models import employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields= '__all__'