from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogs(request):
    all_blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': all_blogs})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
