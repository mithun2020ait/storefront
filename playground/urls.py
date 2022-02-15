from django.urls import path
from . import views

# URLCofig
urlpatterns = [
    path('hello/', views.say_hello)
]