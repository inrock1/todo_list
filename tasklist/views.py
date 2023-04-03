from django.shortcuts import render
from django.views import generic

from tasklist.models import Tag


def index(request):
    """View function for the home page of the site."""

    # tags = Tag.objects.count()
    # num_cars = Car.objects.count()
    # num_manufacturers = Manufacturer.objects.count()
    #
    # num_visits = request.session.get("num_visits", 0)
    # request.session["num_visits"] = num_visits + 1
    #
    # context = {
    #     "num_drivers": num_drivers,
    #     "num_cars": num_cars,
    #     "num_manufacturers": num_manufacturers,
    #     "num_visits": num_visits + 1,
    # }

    # return render(request, "tasklist/index.html", context=context)
    return render(request, "tasklist/index.html")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "tasklist/tag_list.html"
    paginate_by = 5


