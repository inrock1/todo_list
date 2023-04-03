from django.urls import path

from .views import (
    TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    TaskListView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    # path("task/<int:pk>/complete/", views.task_complete, name="task_complete"),
    # path("task/<int:pk>/undo/", views.task_undo, name="task_undo"),
    path("tags/", TagListView.as_view(), name="tag-list",),
    path("tags/create/", TagCreateView.as_view(), name="tag-create",),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update",),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete",),
]

app_name = "tasklist"
