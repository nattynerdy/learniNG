from django.urls import path
from content import views

urlpatterns = [
    path("<int:id>/edit", views.edit_content, name="edit_content"),
    path("add", views.create_content, name="add_content")
]