from django.contrib import admin
from django.urls import path,include
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('asosiy/',include('asosiy.urls')),
    path('static/',include('statistika.urls')),

]
