from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from .models import User
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name,last_name,username,email,password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,'Your account has been successfully registered.')
            return redirect('registerUser')
    else:
        form = UserRegistrationForm()
    context = {"form":form,}
    return render(request,'accounts/registerUser.html',context)

def registerRestaurant(request):
    return render(request,'accounts/registerRestaurant.html')
