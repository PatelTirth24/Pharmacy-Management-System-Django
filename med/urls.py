
from django.urls import path
from med import views
urlpatterns = [
  
    path('add/', views.medi,name='add'),
     
]