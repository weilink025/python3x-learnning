from django.urls import path,re_path
from . import views
app_name = 'tsproject'
urlpatterns = [
    path('index/', views.index ),
    path('<int:id>/',views.show,name='show')
]