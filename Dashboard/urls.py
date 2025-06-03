"""
URL configuration for Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from api.login.login_view import login_view
from api.home.home_view import home_view
from api.dashboard.views_dashboard import dashboard_view
from api.register.register_view import register_view
from api.color.color_view import color_view
from api.typography.typography_view import typography_view
from api.views import feather_icons
from api.views import sample_page
from api.views import logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login_vista'),
    path('register/', register_view, name='register_view'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('colores/', color_view, name='color_view'),
    path('typography/', typography_view, name='typography_view'),
    path('feather-icons/', feather_icons, name='feather_icons'),
    path('sample-page/', sample_page, name='sample_page'),
    path('logout/', logout_view, name='logout'),
]





