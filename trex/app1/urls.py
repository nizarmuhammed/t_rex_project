from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('index/<int:id>',views.index,name='index'),
    path('genre/<int:id>',views.genre,name='genre'),
    path('contact/<int:id>', views.contact, name='contact'),
    path('about/<int:id>', views.about, name='about'),
    path('logout/',views.logoutpage,name='logout'),
    path('setoption', views.setoption, name='setoption'),
    path('allmovies/<int:id>', views.allmovies, name='allmovies'),
    path('search', views.search, name='search'),
    path('showmovies/<int:movie_id>/<int:id>', views.showmovies, name='showmovies'),
    path('video/<int:movie_id>/<int:id>', views.video, name='video'), 

    path('watchlist/<int:id>/', views.watchlist, name='watchlist'),
    path('addwatchlist', views.addwatchlist, name='addwatchlist'),
   

    path('showprofile/<int:id>/',views.showprofile,name='showprofile'),
  
]