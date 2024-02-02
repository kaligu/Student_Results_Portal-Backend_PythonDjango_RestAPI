from rest_framework import serializers
from .models import school

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = school
        fields = ['id', 'name']