"""
URL configuration for frontload project.

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
from  frontapp  import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.main,name='main'),
    path('contact/',views.contact,name='contact'),
    path('pmodel/',views.pmodel,name='model'),
    path('omodel/',views.omodel,name='ordermodel'),
    path('oForm/',views.oForm),
    path('pForm/',views.pForm),
    path('dele/<int:id>',views.dele),
    path('pdelete/<int:id>',views.pdelete),
    path('pupdate/<int:id>',views.pupdate),
    path('update/<int:id>',views.update)
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)