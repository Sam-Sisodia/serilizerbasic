from   rest_framework import serializers
from . models import *
class UserSerlizer(serializers.Serializer):
    username = serializers.CharField(max_length = 299)
    password =  serializers.CharField(max_length = 299)





class Empserializer((serializers.Serializer)):
    name = serializers.CharField(max_length=230)
    address = serializers.CharField(max_length=230)

    def create(self, validated_data):
        print("Creta me thod call =====")
        return Emp.objects.create(**validated_data)




class courseserializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields = ['id','name','dis']
        

