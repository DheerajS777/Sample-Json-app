
from django.urls import path
from . import views
urlpatterns=[
path("",views.activity_data,name="ActivityPeriod data"),
]