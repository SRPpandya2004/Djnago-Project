

# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views

from django.urls import path
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("series", views.series, name='series'),
    path("documentery", views.docu, name='documentery'),
    # Use Django’s built-in LoginView with your custom login template.
    path("login", auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    # LogoutView automatically logs out and can redirect to the login page.
    path("logout", auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("signup", views.signup, name='signup'),


]


# from django.contrib import admin
# from django.urls import path
# from home import views

# urlpatterns = [

#     path("", views.index,name='home'),
#     path("series", views.series ,name='series'),
#     path("documentery", views.docu,name='documentery'),
#     path("login", views.login ,name='login'),
#     path("signup", views.signup,name='signup')
# ]