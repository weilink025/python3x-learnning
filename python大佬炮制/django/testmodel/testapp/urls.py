from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
path('hello/<int:id>', views.show),
]
