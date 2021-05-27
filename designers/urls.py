from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpagefunction,name="mainpaged"),
    path('logind/', views.loginfunction, name="logind"),
	path('checklogind/', views.checklogin, name="checklogind"),
	path('logoutd/', views.logoutUserfunction, name="logoutd"),
	path('mainpaged/', views.mainpagefunction, name="mainpaged"),
    path('homed/', views.homefunction, name="homed"),
	path('aboutd/', views.aboutusfunction, name="aboutd"),
	path('mensfashiond/', views.mensfashionfunction, name="mensfashiond"),
	path('womensfashiond/', views.womensfashionfunction, name="womensfashiond"),
    path('allproductsd/', views.allproductsfunction, name="allproductsd"),
	path('addproductd/',views.addproductPage,name="addprodctsd"),
   
]