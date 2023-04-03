from django.shortcuts import render
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





# def index(request):
#     """View function for the home page of the site."""

    # tags = Tag.objects.count()
    # num_cars = Car.objects.count()
    # num_manufacturers = Tag.objects.count()
    #
    # num_visits = request.session.get("num_visits", 0)
    # request.session["num_visits"] = num_visits + 1
    #
    # context = {
    #     "num_drivers": num_drivers,
    #     "num_cars": num_cars,
    #     "num_tags": num_tags,
    #     "num_visits": num_visits + 1,
    # }

    # return render(request, "tasklist/index.html", context=context)
    # return render(request, "tasklist/index.html")
