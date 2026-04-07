from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.models import Todo


class TodoListView(ListView):
    queryset = Todo.objects.all()
    template_name = 'apps/todo-list.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        qs = super().get_queryset()

        if _search := self.request.GET.get('search'):
            qs = qs.filter(Q(title__icontains=_search))

        return qs


class TodoDetailView(DetailView):
    queryset = Todo.objects.all()
    template_name = 'apps/todo-detail.html'