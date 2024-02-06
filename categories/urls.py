from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'categories'


urlpatterns = [
    path('', views.categories_list_api),
    path('detail_information_card/<int:card_id>/', views.detail_information_card),
]