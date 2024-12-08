from django.urls import path
from . import views

## for fetch to server using urls.py project
urlpatterns = [
    path('', views.hello, name='home'),
    path('update_task/<str:pk>/', views.update_task,name='update'),
    path('delete_task/<str:pk>/', views.delete_task,name='delete'),
]