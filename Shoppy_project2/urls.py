from django.contrib import admin
from django.urls import path, include
from Shoppy_website2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Shoppy_website2.urls')),
    path('', views.Productview.as_view(), name='home'),
    
]
