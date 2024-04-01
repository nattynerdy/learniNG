from django.urls import path
from courses import views

urlpatterns = [
    path("", views.courses_main, name="list_courses"),
    path("<int:id>", views.one_course, name="show_course"),
    path("<int:id>/edit", views.edit_course, name="edit_course"),
    path("add", views.add_course, name="add_course")
]