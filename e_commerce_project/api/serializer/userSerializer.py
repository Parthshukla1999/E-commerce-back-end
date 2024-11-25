from rest_framework import serializers
from api.model.userModel import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","age","email","username","is_active","created_at"]