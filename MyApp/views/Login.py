from django.contrib.auth.hashers import make_password, check_password
from django.http import request
from django.shortcuts import render, redirect
from django.views import  View

from MyApp.models.Customer import Customer


class Login(View):
    def get(self,request):
        return render(request, 'Delicious/login.html')



    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_Customer_by_email(email)
        print(email, password)
        error_message = None

        if customer:
            flage = check_password(password, customer.password)
            if flage:
                request.session['customer'] = customer.id
                # request.session['email'] = customer.email
                return redirect('home')
            else:
                error_message = 'email or Password Invalid'
        else:
            error_message = 'email or Password Invalid'
        # print(email, password)
        return render(request, 'Delicious/login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('home')