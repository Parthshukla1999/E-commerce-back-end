from api.models.userModel import UserModel
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
            error_message = f"Exception Type: {exc_type}, File Name: {fname}, Line Number: {exc_tb.tb_lineno}, Error: {str(e)}"
            
            # Log the error using the 'error_log' logger
            logger_error.error(error_message)
            return {"data":None,"message":str(e),"status":400}
        

    def login(self, request):
        print(request.data)
        logger_demo.debug(f"request:{request.data}")
        try:
            user = UserModel.objects.get(username = request.data["username"])
            logger_demo.debug(f"user values:{user.password,user.username}")
        except UserModel.DoesNotExist:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            error_message = f"Exception Type: {exc_type}, File Name: {fname}, Line Number: {exc_tb.tb_lineno}, Error: user does not exist"
            
            # Log the error using the 'error_log' logger
            logger_error.error(error_message)
            return {"data":None,"message":"user with this email or username does not exist","status":400}
        try:
            if user:
                logger_demo.debug(f"user password check{"password"}")
                if check_password(request.data["password"], user.password):
                    ref_token = RefreshToken.for_user(user)
                    access_token = str(ref_token.access_token)
                    serializer = UserSerializer(user)
                    data = serializer.data
                    data["token"]=access_token
                    print(data,"00000000000000000")
                    return {"data":data,"message":"user login ","status":200}
                else:
                    return {"data":None,"message":"Incorrect password","status":400}
                
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            error_message = f"Exception Type: {exc_type}, File Name: {fname}, Line Number: {exc_tb.tb_lineno}, Error: {str(e)}"
            
            # Log the error using the 'error_log' logger
            logger_error.error(error_message)
            return {"data":None,"message":"user with this email or username does not exist","status":400}






