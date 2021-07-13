from django.shortcuts import render
from .models import Blog
# Create your views here.


def homepage(request):
    context ={
        "blogs":Blog.objects.all()
    }
    return render(request,'blogs/home.html',context)