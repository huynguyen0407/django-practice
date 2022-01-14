from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index1"),

    path('update_task1/<str:pk>/', views.updateTask, name='update_task1'),

    path('delete/<str:pk>/', views.deleteTask, name='delete')
]