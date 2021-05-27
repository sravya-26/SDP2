from django.shortcuts import render
from django.shortcuts import render,redirect
from .form import ImageForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template
from .models import * 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
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
from django.contrib.auth.models import User, auth
import json
import datetime
from .form import ImageForm
from .models import Image
from SDP2BTT.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.auth import logout


# @login_required(login_url='login')
def mainpagefunction(request):
	return render(request,"mainpaged.html")

def homefunction(request):
    # if request.method == "POST":
    #     form = ImageForm(data=request.POST, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         obj = form.instance
    #         return render(request, "homed.html",{"obj":obj})
    # else:
    #     form = ImageForm()
    #     img = Image.objects.all()
    img = Image.objects.all()
    form=ImageForm()
    if "addproduct" in request.POST:
        form=ImageForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print("hello")
            form.save()
    return render(request,"homed.html",{"img":img,'form':form})


def addproductPage(request):
    form=ImageForm()
    return render(request,'homed.html',{'img':form})


def loginfunction(request):
    return render(request, 'logind.html')


def checklogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        flag = username == 'admin' and password == 'admin'
        if flag:
            auth.login(request, user)
            return render(request,'mainpaged.html')
        else:
            return HttpResponse("Login Invalid")
    else:
        return render(request, 'mainpaged.html')

# def checklogin(request):
#     if request.method == "POST":
#         uname = request.POST["username"]
#         pwd = request.POST["password"]
#         flag = uname == 'admin' and pwd == 'admin'
#         if flag:
#             return render(request,"mainpaged.html")
#         else:
#             return HttpResponse("Login Invalid")
#     else:
#         return render(request,"mainpaged.html") 


def logoutUserfunction(request):
    logout(request)
    return redirect('logind')

def aboutusfunction(request):
	return render(request,"aboutd.html")

def allproductsfunction(request):
    img = Image.objects.all()
    return render(request,"productsd.html",{'img':img})

def mensfashionfunction(request):
    img = Image.objects.filter(category="MensFashion")
    return render(request,"mensfashiond.html",{'img':img})

def womensfashionfunction(request):
    img = Image.objects.filter(category="WomensFashion")
    return render(request,"womensfashiond.html",{'img':img})



# def cart(request):
# 	data = cartData(request)

# 	cartItems = data['cartItems']
# 	order = data['order']
# 	items = data['items']

# 	context = {'items':items, 'order':order, 'cartItems':cartItems}
# 	return render(request, 'store/cart.html', context)


# def cart(request):
#     id = request.POST.get('id')


# def product(request):
#     items = Item.objects.all()
#     return render(request, 'products.html', {'items':items})


