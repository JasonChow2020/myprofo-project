from django.shortcuts import render, get_object_or_404

from .models import Blog #***** that's bring blog in models as reference to the html below

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs}) #refer to this html and 'blogs' also as parameters

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'d_blog': detailblog}) #refer to this html and 'd_blog' also as parameters
