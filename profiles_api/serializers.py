from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 15)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'} #To show dots not text while typing password
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password) #set_password is used to hash password.

        return super().update(instance, validated_data) #Removed password from validated_data and added password hash to instance.