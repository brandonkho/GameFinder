from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.urlresolvers import reverse

# Create your views here.
from .forms import LoginForm, RegisterForm

def login_view(request):
    #next = request.GET.get('next')
    #print(next)
    #print("DONG")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            #if next:
                #return redirect(next)
            return redirect('/')
    else:
        form = LoginForm()
    template = 'login.html'
    context = {'form': form}
    return render(request, template, context)

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
    template = 'login.html'
    context = {'form': form}
    return render(request, template, context)

def logout_view(request):
    logout(request)
    template = 'form.html'
    context = {}
    url = reverse('index')
    #return render(request, template, context)
    return HttpResponseRedirect(url)