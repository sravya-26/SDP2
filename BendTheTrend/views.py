from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template
from .models import * 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact,cart as ct
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm, UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Customer
from django.contrib.auth.models import User, auth
import json
import datetime
from .utils import cookieCart, cartData, guestOrder
from designers.models import Image
from django.contrib.auth import logout

# @login_required(login_url='login')
def index(request):
	return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return render(request,'index.html')
        else:
            err = "invalid credentials"
            return render(request, 'error.html', {'err': err})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user = User.objects.create_user(username=username, password=pass1, email=email)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')

def logoutUser(request):
	logout(request)
	return redirect('login')


def contact(request):
	if request.method == 'POST':
		form = Contact()
		form.name = request.POST['name']
		form.email = request.POST['email']
		form.message = request.POST['desc']
		if form.name == "" or form.email == "" or form.message == "":
		    return render(request, 'contact.html')
		else:
			form.save()
			return render(request, 'contact.html')
	else:
		return render(request, 'contact.html')
		
		

def aboutus(request):
	return render(request,"about.html")

def allproducts(request):
	img=Image.objects.all()
	return render(request,"products.html",{'img':img})

# def allproducts(request):
# 	customer = request.user.customer
# 	order, created = Order.objects.get_or_create(customer=customer, complete=False)
# 	items = order.orderitem_set.all()
# 	cartItems = order.get_cart_items
# 	img = Image.objects.all()
# 	context = {'img':img, 'cartItems':cartItems}
# 	return render(request, 'products.html', context)


def mensfashion(request):
    img = Image.objects.filter(category="MensFashion")
    return render(request,"mensfashion.html",{'img':img})

def womensfashion(request):
    img = Image.objects.filter(category="WomensFashion")
    return render(request,"womensfashion.html",{'img':img})


def cart(request):
	# data = cartData(request)
	# user = request.user
	# cartItems = data['cartItems']
	# order = data['order']
	# items = data['items']
	# context = {'items':items, 'order':order, 'cartItems':cartItems}
	# return render(request, 'cart.html', context)
	user = request.user
	items = ct.objects.filter(user=user.id).distinct()
	li = []
	for i in items:
		li.append(i)
	sum = 0
	for j in li:
		details = {
			'price':j.i.price
		}
		sum  = sum + details['price']
	context = {'items':items,'sum':sum}
	return render(request, 'cart.html',context)

def addToCart(request):
    id = request.POST.get('id')
    i = Image.objects.get(id=id)
    user = request.user
    c = ct(user=user, i=i)
    c.save()
    return redirect('cart')

# def cart(request):
# 	if request.user.is_authenticated:
# 		customer = request.user.customer
# 		order, created = Order.objects.get_or_create(customer=customer, complete=False)
# 		items = order.orderitem_set.all()
# 	else:
# 		items = []

# 	context = {'items':items}
# 	return render(request,'cart.html',context)


# def checkout(request):
# 	data = cartData(request)
	

def checkout(request):
	user = request.user
	items = ct.objects.filter(user=user.id).distinct()
	li = []
	for i in items:
		li.append(i)
	sum = 0
	for j in li:
		details = {
			'price':j.i.price
		}
		sum  = sum + details['price']
	context = {'items':items,'sum':sum}
	return render(request,'checkout.html',context)

# 	cartItems = data['cartItems']
# 	order = data['order']
# 	items = data['items']

# 	context = {'items':items, 'order':order, 'cartItems':cartItems}
# 	return render(request, 'store/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

