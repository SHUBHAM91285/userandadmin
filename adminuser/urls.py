from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginuser", views.loginuser, name="loginuser"),
    path("loginadmin", views.loginadmin, name="loginadmin"),
    path("registeradmin", views.registeradmin, name="registeradmin"),
    path("registeruser", views.registeruser, name="registeruser"),
    path("homeadmin", views.homeadmin, name="homeadmin"),
    path("homeuser", views.homeuser, name="homeuser"),
    path("addapp", views.addapp, name="addapp"),
    path("mapuserapp", views.mapuserapp, name="mapuserapp"),
    path("info/<int:id>", views.info, name="info"),
    path("appuser/<int:id>", views.appuser, name="appuser"),
]