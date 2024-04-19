from django.urls import path
from .views import *

urlpatterns = [
    
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("add-std/", std_add, name="add_std"),
    path("delete-std/<int:roll>/", delete_std, name="delete_std"),
    path("update-std/<int:roll>/", update_std, name="update_std"),  # Use update_std view here
    path("do-update-std/<int:roll>/", do_update_std, name="do_update_std"),  # Use do_update_std view here
]
