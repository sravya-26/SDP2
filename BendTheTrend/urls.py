from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('/login', views.login, name="login"),
	path('/register', views.register, name="register"),
	path('/logout', views.logoutUser, name="logout"),
	path('/index', views.index, name="index"),
	path('/about', views.aboutus, name="about"),
	path('/contact', views.contact, name="contact"),
	path('/mensfashion', views.mensfashion, name="mensfashion"),
	path('/womensfashion', views.womensfashion, name="womensfashion"),
    path('/allproducts', views.allproducts, name="allproducts"),
	path('/cart', views.cart, name="cart"),
	path('/checkout', views.checkout, name="checkout"),
	path('/update_item', views.updateItem, name="update_item"),
	path('/process_order', views.processOrder, name="process_order"),
	path('addToCart', views.addToCart, name="addToCart")

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

