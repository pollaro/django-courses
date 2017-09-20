from django.shortcuts import render, redirect
from .models import Courses

def index(request):
    context = {
        'courses':Courses.objects.all()
    }
    return render(request,'courses/index.html',context)

def destroy(request,id):
    course = {
        'course':Courses.objects.get(id=id)
    }
    return render(request,'courses/destroy.html',course)

def addCourse(request):
    Courses.objects.create(name=request.POST['courseName'],desc=request.POST['descField'])
    return redirect(index)

def confirm(request,id):
    c = Courses.objects.get(id=id)
    c.delete()
    return redirect(index)
