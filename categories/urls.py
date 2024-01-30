from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'categories'


urlpatterns = [
    path('', views.render_categories_list),
]