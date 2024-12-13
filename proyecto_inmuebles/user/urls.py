from django.urls import path
from . import views



app_name = "user"

urlpatterns = [
    path("profile/", views.update_profile, name="profile"),
    path("login/", views.log_in, name="login"),
    path("signup/",views.sign_up, name="signup"),
    path("logout/",views.log_out,name="logout"),
    path("arrendatario/", views.arrendatario, name="arrendatario"),
    path("propietario/", views.propietario, name="propietario"),
]
