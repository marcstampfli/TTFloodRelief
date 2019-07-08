from django.urls import path, include
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index),
    path('detail/<int:location_id>/', views.detail),
    url(r'^search/', include('haystack.urls')),
    path('get_listed/', views.get_listed),
]
