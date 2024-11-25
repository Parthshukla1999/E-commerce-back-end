from api.services.userService import UserService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
user_obj = UserService()


class SignUp(APIView):
    permission_classes =[AllowAny]
    def post(self, request):
        result = user_obj.signup(request)
        return Response(result, status=result["status"])
    

class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        result = user_obj.login(request)
        return Response(result, status=result["status"])
    



