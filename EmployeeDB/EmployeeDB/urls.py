"""EmployeeDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from staff.views import UploadProfile, GetAllProfiles, home, login, logout_view, login_call, remove, edit, update


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-profile/', UploadProfile.as_view(), name="upload-profile"),
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('get-all-profiles/', GetAllProfiles.as_view(),
         name='get-all-profiles'),
    path('remove/<int:empcode>', remove, name='remove'),
    path('edit/<int:empcode>', edit, name='edit'),
    path('update/<int:empcode>', update, name='update'),
    path('login_call/', login_call, name='login_call'),
    path('logout_view/', logout_view, name='logout_view'),
]
