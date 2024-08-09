from django.contrib import admin
from .models import  Profile,Movies, Watchlists, History, Subscribe

# Register your models here.

admin.site.register(Profile)
admin.site.register(Movies)
admin.site.register(Watchlists)
admin.site.register(History)
admin.site.register(Subscribe)
