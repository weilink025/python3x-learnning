from django.urls import path,re_path
from . import views


urlpatterns = [
    path('hello/', views.index),
    path('hello/<int:id>',views.show)
]
