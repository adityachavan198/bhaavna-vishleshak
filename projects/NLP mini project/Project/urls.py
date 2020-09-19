from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.index, name="index"),
    path("find", views.find, name="find"),
]
