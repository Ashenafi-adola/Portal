from django.urls import path
from .import views
urlpatterns = [
    path("", views.signin, name="login"),
    path("register/", views.registration , name="register"),
    path("mainRegister/", views.mianRegistration , name="mainregister"),
    path("mainLogin/", views.mainLogin , name="mainLogin"),
    path("home/", views.home, name="home"),
    path("studProfile/", views.studentProfile, name="studProfile"),
    path("applicant/", views.appilicant, name="applicnat"),
    path("complete/", views.Additional, name="complete"),
    path("success/",views.success, name="success")
]

