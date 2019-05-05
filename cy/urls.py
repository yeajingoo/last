from django.urls import path
from . import views
from products import views

urlpatterns = [
    path('holy/', views.holy),
]