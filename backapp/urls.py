from django.urls import path
from backapp  import views

urlpatterns =[
    path('login/',views.loginpage),
    path('signup/',views.signup),
    path('logout/',views.logoutpage,name="logout"),
]