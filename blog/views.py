from django.shortcuts import render, get_object_or_404 # this will show a particular object(blog), It it couldn't found it will show 404 page
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5] #Blog.objects.all()  #here they will show top 5 blogs in order by recent date
    return render(request,'blog/all_blogs.html',{'blogs':blogs})
def detail(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)#pk is for database primary key(here is blog id /blog serial number)
    return render(request,'blog/detail.html',{'blog':blog})
