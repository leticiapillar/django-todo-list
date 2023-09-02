from typing import Any, Dict
from django.urls import reverse
from django.db.models.query import QuerySet
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from .models import ToDoList, ToDoItem

# Create your views here.
class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: 
        context =  super().get_context_data(**kwargs)
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ListCreate, self).get_context_data(**kwargs)
        context["title"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date"
    ]

    def get_initial(self) -> Dict[str, Any]:
        initinal_data = super(ItemCreate, self).get_initial()
        todo_list =  ToDoList.objects.get(id=self.kwargs["list_id"])
        initinal_data["todo_list"] = todo_list
        return initinal_data

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ItemCreate, self).get_context_data(**kwargs)
        todo_list =  ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context
    
    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(ItemUpdate, self).get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        context["title"] =  "Edit item"
        return context

    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.todo_list_id])
