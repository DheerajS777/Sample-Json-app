from django.urls import path
from . import views
urlpatterns=[
path("",views.user_data,name="User data"),
]