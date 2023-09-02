from django.urls import path
from todo_app import views

urlpatterns = [
    path("", 
         views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/",
         views.ItemListView.as_view(), name="list"),
     # CRUD patterns for ToDOLists
     path("list/add/", views.ListCreate.as_view(), name="list-add"),
     # CRUD patterns for ToDOItems
     path(
         "list/<int:list_id>/item/add/",
         views.ItemCreate.as_view(),
         name="item-add",
     ),
     path(
         "list/<int:list_id>/item/<int:pk>/",
         views.ItemUpdate.as_view(),
         name="item-update",
     ),
]