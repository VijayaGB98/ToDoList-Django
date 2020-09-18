from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create'),
    path('edit/<str:pk>/', views.edit_or_delete_task, name='edit'),
    path('complete/<str:pk>', views.complete_task, name='complete')
]