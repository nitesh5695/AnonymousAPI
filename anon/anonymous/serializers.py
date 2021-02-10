from rest_framework import serializers
from .models import customer_model
from django.contrib.auth.models import User

class customer_serializer(serializers.ModelSerializer):
 class Meta:
  model = customer_model
  fields = ['id', 'name', 'mobile', 'customer_type']

  

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

            return user
        except KeyError:
            raise serializers.ValidationError("all fields  are required")