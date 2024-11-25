from api.model.userModel import User
from api.serializer.userSerializer import UserSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
import logging
import sys , os


logger=logging.getLogger(__name__)
logger=logging.getLogger("django")
logger_demo=logging.getLogger("demo_log")
logger_error=logging.getLogger("error_log")



class UserService():
    def signup(self,request):
        try:
            password = request.data["password"]
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid():
                user  = serializer.save()

                user.set_password(password)
                user.save()

            return {"data":serializer.data,"message":"user signup successfully","status":200}
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger_error.error(exc_type, fname, exc_tb.tb_lineno)
            return {"data":None,"message":str(e),"status":400}
        

    def login(self, request):
        try:
            user = User.objects.get(Q(email = request.data["email"])| Q(username = request.data["username"]))
        except User.DoesNotExist:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger_error.error(exc_type, fname, exc_tb.tb_lineno)
            return {"data":None,"message":"user with this email or username does not exist","status":400}
        try:
            if user:
                password = check_password(user.password, request.data["password"])
                if password:
                    ref_token = RefreshToken.for_user(user)
                    access_token = str(ref_token.access_token)
                    serializer = UserSerializer(user)
                    data = serializer.data
                    data["token"]=access_token
                    return {"data":data,"message":"user login ","status":200}
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger_error.error(exc_type, fname, exc_tb.tb_lineno)
            return {"data":None,"message":"user with this email or username does not exist","status":400}






