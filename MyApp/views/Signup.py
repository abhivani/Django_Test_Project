from django.contrib.auth.hashers import make_password, check_password
from django.http import request
from django.shortcuts import render, redirect
from django.views import  View

from MyApp.models.Customer import Customer


class Signup(View):
    def get(self,request):
        return render(request, 'Delicious/signup.html')


    def post(self,request):
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        number = postData.get('number')
        password = postData.get('password')
        # validation
        value = {
            'name': name,
            'email': email,
            'number': number,
            'password': password
        }
        print(value)
        error_message = None
        customer = Customer(name=name,
                            number=number,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)
        print("before error message")
        if not error_message:
            print(name, email, number, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
            print('after error message')
        else:
            data = {
                'error': error_message,
                'values': value
            }

        return redirect('login')

    def validateCustomer(self,customer):
        error_message = None;
        if (not customer.name):
            error_message = "First Name Required !!"
        elif len(customer.name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.number:
            error_message = 'Phone Number required'
        elif len(customer.number) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) <= 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
            # saving

        return error_message
