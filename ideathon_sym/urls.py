"""
URL configuration for ideathon_sym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('home/',views.home),
    path('department/',views.department),
    path('symposium/',views.symposium),
    path('domain/',views.domain),
    path('agriculture/',views.agriculture),
    path('transport/',views.transport),
    path('space/',views.space),
    path('resource/',views.resource),
    path('healthcare/',views.healthcare),
    path('data_privacy/',views.data_privacy),
    path('problem/',views.problem),
    path('disaster/',views.disaster),
    path('education/',views.education),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

