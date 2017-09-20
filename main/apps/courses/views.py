from django.shortcuts import render, redirect
from .models import Courses

def index(request):
    return render(request,'courses/index.html')

def destroy(request,id):
    return redirect(index)
