from django.urls import path
from . import views

urlpatterns = [
     # path('', views.index, name='index'),
      path('', views.preloans, name='preloans'),
      path('about/', views.about, name='about'),
  #    path('main/', views.main, name='main'),
      path('services/', views.services, name='services')
      
]
