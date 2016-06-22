from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.core.urlresolvers import reverse
from .models import Post
from .forms import PostForm
from .filter import PostFilter

import urllib
import json

def home(request):
    if request.user.is_authenticated():
        username_is = "Jamal"
        context = {"user": request.user}
    else:
        context = {"user": request.user}
    
    template = 'base.html'  
    return render(request, template, context)
    #return HttpResponse("Hello, world. You're at the home index.")

def index(request):
    #sports = {'basketball': 'images/basketball.png', 'soccer': 'images/football.png', 'tennis': 'images/tennis.png', 'volleyball': 'images/volleyball.png'}
    #posts = Post.objects.order_by('-created_date')
    posts = PostFilter(request.GET, queryset=Post.objects.order_by('-created_date'))
    template = 'posts/posts.html'
    context = {'posts': posts, 'user': request.user}
    return render(request, template, context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, post_id):
    template = 'posts/detail.html'
    post = get_object_or_404(Post, id=post_id)

    location_str = post.location
    address= location_str.replace(' ', '+')
    city = post.city.replace(' ', '+')
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s+%s" % (address, city)
    response = urllib.request.urlopen(url)
    jsongeocode = response.read().decode('utf-8')
    jsongeocode = json.loads(jsongeocode)
    latitude = jsongeocode['results'][0]['geometry']['location']['lat']
    longitude = jsongeocode['results'][0]['geometry']['location']['lng']


    context = {'post': post, 'latitude': latitude, 'longitude': longitude}
    return render(request, template, context)
    #return HttpResponse("Youre %s" % post_id)

@login_required(login_url='/login/')
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        #form.fields['author'].widget.attrs['value'] = request.user

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            url = reverse('index')
            return HttpResponseRedirect(url)

    else:
        form = PostForm()

    
    context = {'form': form, 'user': request.user}
    template = 'posts/new.html'
    return render(request, template, context)
    #return HttpResponse("Make new Post")



def add_user(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.joined_users.add(request.user)
    post.save()
    url = post.get_absolute_url()
    return HttpResponseRedirect(url)

def filtered_list(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'posts/list.html', {'filter': f})