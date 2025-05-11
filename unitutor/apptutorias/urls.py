from django.urls import path
from . import views

urlpatterns = [
path("hola/",views.index.as_view(), name="indexx"),
path("signup/",views.SignUpView.as_view(),name="signup"),
path("Login/",views.LoginView.as_view(),name="Login"),
path("panel-profesores/",views.paneProfesores.as_view(),name="panelp")
]