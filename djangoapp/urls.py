
from django.contrib import admin
from django.urls import path, include
from biblioteca.views import home

urlpatterns = [
    path('', home,name='home'),
    path('admin/', admin.site.urls),
    path('livros/', include('biblioteca.urls')), 
    
    
]
