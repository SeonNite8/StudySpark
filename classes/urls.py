from django.urls import path
from . import views


urlpatterns = [
    path('classmates/', views.classmates ,name = 'classmates'),
    path('classroom/', views.classroom ,name = 'classroom'),
    path('create_class/', views.create_class ,name = 'create_class'),
    path('join_classes/', views.join_class ,name = 'join_classes'),
    path('assignments/', views.assignments ,name = 'assignments'),

]