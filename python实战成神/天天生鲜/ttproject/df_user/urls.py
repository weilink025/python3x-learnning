from django.urls import path
from . import views
urlpatterns = [
    path('test/',views.test ),
    path('register/',views.register ),
    path('register_handle/',views.register_handle),
    path('register_exist/',views.register_exist),
    path('login/',views.login),
    path('login_handle/',views.login_handle ),
    path('logout/',views.user_logout ),
    path('user_center_info/',views.user_center_info ),
    path('user_center_order/',views.user_center_order ),
    path('user_center_site/',views.user_center_site ),


]
