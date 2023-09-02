from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import ToDoList, ToDoItem

# Create your views here.
class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "dodo_app/todo_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: 
        context =  super().get_context_data(**kwargs)
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context