


"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api$', views.API , name='api'),
    url(r'^api/mydevices$', views.mydevices , name='index'),
    url(r'^api/qr$', views.qr , name='qr'),
    url(r'^api/form$', views.form , name='form'),
    url(r'^api/reg$', views.reg , name='reg'),
    url(r'^api/add$', views.add_device , name='new'),

]
