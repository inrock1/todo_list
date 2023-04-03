from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from tasklist.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasklist/index.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasklist:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasklist:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasklist:index")



class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "tasklist/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasklist:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasklist:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasklist:tag-list")


def complete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_done = True
    task.save()
    return redirect('tasklist:index')


def undo_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_done = False
    task.save()
    return redirect('tasklist:index')

