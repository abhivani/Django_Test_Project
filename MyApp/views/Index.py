from django.http import request
from django.shortcuts import render, redirect
from django.views import  View


class Index(View):
    def get(self,request):
        print("You are : ",request.session.get('email'))
        return render(request, 'Delicious/index.html')
