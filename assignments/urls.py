from django.urls import path
from .views import upload_assignment

urlpatterns = [
    path('upload-assignment/', upload_assignment, name='upload_assignment'),
]
