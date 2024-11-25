from rest_framework import serializers
from api.models.userModel import UserModel



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["first_name","last_name","age","email","username","is_active","created_at"]