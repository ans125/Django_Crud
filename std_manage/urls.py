from django.contrib import admin
from django.urls import path, include
from std import views  # Assuming you have a views.py file in your std app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('std/', include('std.urls')),
    path('', views.home, name='home'),  # Define a path for the root URL
]
