from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('proba/', views.proba),
    path('updateAdd/', views.updateAdd, name = 'gogo'),
    path('updateAdd2/<str:pk>/', views.updateAdd2, name = 'gogo2'),
    path('error/', views.error),
]