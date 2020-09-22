from rest_framework import serializers
from . models import Employee


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
#        fields = {'firstName', 'lastName'}
    fields = "__all__"
