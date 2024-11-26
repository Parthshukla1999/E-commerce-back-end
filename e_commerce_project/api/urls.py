from django.urls import path
from api.view import userView
urlpatterns =[

    #user onboarding
    path("sign-up/",userView.SignUp.as_view()),
    path("login/",userView.Login.as_view()),
    path("logout/",userView.logout.as_view()),
    path("get-user-details/",userView.GetUserDetails.as_view()),
    path("update-user-details/",userView.UpdateUserDetails.as_view()),
    path("user-deactive/",userView.UserDeative.as_view()),

]