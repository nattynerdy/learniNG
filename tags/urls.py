from django.urls import path
from tags import views

urlpatterns = [
    path("", views.list_tags, name="list_tags"),
    path("add", views.create_tag, name="add_tag"),
    path("<int:id>/edit", views.edit_tag, name="edit_tag")
]