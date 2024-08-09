
from aiohttp import request
from django.shortcuts import get_object_or_404, render,  redirect
from .models import Movies, Profile, Watchlists, History
from django.core.mail import send_mail
from .models import Subscribe
from django.contrib.auth import logout
from .models import Profile
from django.http import Http404, JsonResponse, HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app1.models import Movies, Watchlists, Profile
import requests


# Create your views here.
def login(request):
    if request.method=='POST':
        Email=request.POST.get('email')
        Pass1=request.POST.get('password1')
        print(Email)
        print(Pass1)
        # user=Profile.objects.get(email=Email,password1=Pass1)
        # if user is not None:
        #     login(request,user)
        #     return redirect('index')
        try:
                user=Profile.objects.get(email=Email)
                print(user.password1)
                if not user:
                    messages.warning(request,'Email does not exist')
                    return redirect('/')
                elif Pass1!=user.password1:
                    messages.warning(request,'Password Incorrect')
                    return redirect('/')
                else:
                    messages.success(request,'Success')
                    return redirect('/index/%s' % user.id)
        except:
                messages.warning(request,'Email or Password incorrect')
                return redirect('/')
        
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Pass1=request.POST.get('password1')
        Pass2=request.POST.get('password2')
        user = Profile.objects.create(name=Name,email=Email,password1=Pass1,password2=Pass2)
        user.save()
        messages.success(request,'Account Created Successfully.')
        return redirect('login')
    return render (request,'signup.html')


def logoutpage(request):
    logout(request)
    return redirect('login') 
    

def index(request,id):
    user=Profile.objects.get(id=id)
    return render(request,'index.html',{'user':user})

def genre(request,id):
    user=Profile.objects.get(id=id)
    movie = Movies.objects.all()
    return render(request, 'genre.html',{'movie':movie,'user':user})

def allmovies(request,id):
    user=Profile.objects.get(id=id)
    movie = Movies.objects.all()
    return render(request, 'allmovies.html',{'movie':movie,'user':user})

def showmovies(request, movie_id,id):
    user=Profile.objects.get(id=id)
    movie = Movies.objects.get(pk=movie_id)
    return render(request, 'showmovies.html', {'movie': movie,'user':user})

def video(request, movie_id,id):
    user=Profile.objects.get(id=id)
    movie= Movies.objects.get(pk=movie_id)
    return render(request, 'video.html', {'movie': movie,'user':user})

def watchlist(request, id):
    try:
        user = Profile.objects.get(id=id)
        watchlist_items = Watchlists.objects.filter(user=user)
        return render(request, 'watchlist.html', {'watchlist_items': watchlist_items, 'user': user})
    except Profile.DoesNotExist:
        return render(request, 'error.html', {'message': 'User not found.'})

def addwatchlist(request):
    movie_id = request.POST.get('movie_id')
    user_id = request.POST.get('user_id')  # Assuming you pass the user ID along with the movie ID
    try:
        movie = Movies.objects.get(id=movie_id)
        user = Profile.objects.get(id=user_id)
        
        # Check if the movie is already in the user's watchlist
        if Watchlists.objects.filter(user=user, movie=movie).exists():
            messages.warning(request,'Movie is already in the watchlist.')
            return render(request, 'showmovies.html', {'movie': movie,'user':user})
        else:
            # Add the movie to the user's watchlist
            watchlist_item = Watchlists.objects.create(user=user, movie=movie)
            messages.success(request,'Movie added to watchlist successfully.')
            return render(request, 'showmovies.html', {'movie': movie,'user':user})
    except Movies.DoesNotExist:
        messages.warning(request,'Movie not found.')
        return render(request, 'showmovies.html', {'movie': movie,'user':user})

    

def search(request):
    return render(request, 'search.html')

def contact(request,id):
    user=Profile.objects.get(id=id)
    return render(request, 'contact.html',{'user':user})

def about(request,id):
    user=Profile.objects.get(id=id)
    return render(request, 'about.html',{'user':user})

def settings(request):
    return render(request,'settings.html')

def setoption(request):    
    return render(request, 'setoption.html')



def showprofile(request,id):
    user=get_object_or_404(Profile,pk=id)
    return render(request,'showprofile.html',{'user':user})


