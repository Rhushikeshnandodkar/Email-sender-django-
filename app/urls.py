from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('filter', views.filter, name='filter_results'),
    path('notfound', views.notfound, name='not_found'),
    path('campaign', views.campaign, name='campaign'),
    path('campdetails/<int:pk>', views.campdetails, name='campdetails'),
    path('sendemail/<int:pk>', views.sendemail, name='sendemail'),
    path('thanks', views.thanks, name='thanks'),
]
