from rest_framework import serializers
from api.admin import Todo
# from rest_framework.serializers import ModelSerializer 
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields= '__all__'

