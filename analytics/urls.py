from django.urls import path
from . import views

urlpatterns = [
    path('analytics/', views.save_bar_chart, name='analytics'),
    
]
