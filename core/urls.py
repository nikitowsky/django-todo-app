from django.urls import path

from core import views

urlpatterns = [
    path('todos/', views.TodoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('todos/<int:pk>', views.TodoViewSet.as_view({
        'delete': 'destroy',
    })),
]
