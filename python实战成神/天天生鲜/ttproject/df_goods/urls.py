from django.urls import path
from .import views
urlpatterns = [
    path('',views.index),
    path('goods/detail/',views.detail),
    path('goods/list/<int:product_type_id>/',views.list),
    path('goods/detail/<int:product_id>/',views.detail),
    path('data/',views.datapool),
]