from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('filter', views.filter, name='filter_results'),
]
