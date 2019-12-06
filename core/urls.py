from django.urls import path

from core import views

urlpatterns = [
    path('todos/', views.TodoViewSet.as_view({'get': 'retrieve'})),
]
