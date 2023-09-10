from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('city_list/', views.city_list, name='city_list'),

]