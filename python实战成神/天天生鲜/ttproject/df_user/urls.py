from django.urls import path
from . import views
urlpatterns = [

    path('resigter/',views.register ),
    path('register_handle/',views.register_handle),
    path('register_exist/',views.register_exist),
    path('login/',views.login ),
    path('user_center_info/',views.user_center_info ),
    path('user_center_site/',views.user_center_site ),
    path('register_handle/',views.register_handle ),

]
