from django.urls import path
from . import views
appname = 'tsproject'
urlpatterns = [
    path('a/', views.a ),
]