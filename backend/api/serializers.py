from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

UserModel = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, cleaned_data):

        user_obj = UserModel.objects.create_user(
            email=cleaned_data['email'], password=cleaned_data['password'])
        user_obj.username = cleaned_data['username']
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = UserModel
        fields = ('email', 'password')

    ##
    def check_user(self, cleaned_data):
        user = authenticate(
            username=cleaned_data["email"], password=cleaned_data["password"])
        if not user:
            raise serializers.ValidationError("User not found")

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')
