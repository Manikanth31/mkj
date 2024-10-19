from django.contrib import admin
from django.urls import path
from myapp.views import htop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', htop, name='htop'),
    
]