from api.services.userService import UserService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
import  logging
user_obj = UserService()

logger=logging.getLogger(__name__)
logger=logging.getLogger("django")
logger_demo=logging.getLogger("demo_log")
logger_error=logging.getLogger("error_log")

class SignUp(APIView):
    permission_classes =[AllowAny]
    def post(self, request):
        result = user_obj.signup(request)
        logger_demo.debug("sign up result:",result)
        return Response(result, status=result["status"])
    
class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        result = user_obj.login(request)
        logger_demo.debug(f"login result:{result}")
        return Response(result, status=result["status"])
    
class logout(APIView):
    def get(self, request):
        result = user_obj.logout(request)
        return Response(result, status=result["status"])
    
class GetUserDetails(APIView):
    def get(self, request):
        result = user_obj.user_detials(request)
        return Response(result, status=result["status"])
    
class UpdateUserDetails(APIView):
    def put(self, request):
        result = user_obj.update_user_details(request)
        return Response(result, status=result["status"])
    
class UserDeative(APIView):
    def get(self,request):
        result = user_obj.user_account_deactivate(request)
        return Response(result, status=["status"])
    

    


    



