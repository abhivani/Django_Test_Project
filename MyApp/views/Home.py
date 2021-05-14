from django.http import request
from django.shortcuts import render, redirect
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'Delicious/login.html')

    def post(self, request):
        return render(request, 'Delicious/homeIndex.html')
