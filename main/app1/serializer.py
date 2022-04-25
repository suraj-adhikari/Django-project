from rest_framework import serializers
from app1 import models


class ProjectSerializer(serializers.ModelSerializer):
    pname = serializers.CharField()
    budget = serializers.FloatField()
    class Meta:
        model = models.Employee 
        fields = ["pname", "budget"]


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.dname', allow_null=True,)
    project = ProjectSerializer(many=True, allow_null=True,)
    class Meta:
        model = models.Employee
        fields = ['name', 'joining_date', 'department', 'project']
