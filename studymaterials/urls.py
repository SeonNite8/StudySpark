from django.urls import path
from .views import study_materials

urlpatterns = [
    path('study-materials/', study_materials, name='study_materials'),
]
