from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'categories'


urlpatterns = [
    path('', views.categories_list_api),
    path('cards_list/section/<int:section_id>/group/<int:group_id>/subgroup/<int:subgroup_id>/', views.cards_list_api),
    path('detail_information_card/<int:card_id>/', views.detail_information_card_api),
    path('products_list/<int:card_id>/', views.products_list_api),
]