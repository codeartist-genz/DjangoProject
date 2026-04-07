from django.urls import path

from apps.views import TodoListView, TodoDetailView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('todos/<int:pk>', TodoDetailView.as_view(), name='todo_page'),
]