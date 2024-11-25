from django.urls import path
from api.view import userView
urlpatterns =[
    path("sign-up/",userView.SignUp.as_view()),
    path("login/",userView.Login.as_view()),
]