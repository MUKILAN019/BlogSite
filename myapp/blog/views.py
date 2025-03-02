from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
posts = [
        {'id':1,'title':'Post 1','content':'content of post 1'},
        {'id':2,'title':'Post 2','content':'content of post 2'},
        {'id':3,'title':'Post 3','content':'content of post 3'},
        {'id':4,'title':'Post 4','content':'content of post 4'},
]

def index(request):
    
    return render(request,"index.html",{"posts":posts})

def detail(request,post_id):
    post = next((item for item in posts if item['id']==int(post_id)),None)
    return render(request,"detail.html",{'post':post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_url_name'))

def new_url_view(request):
    return HttpResponse("This is the new Url")