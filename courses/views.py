from django.shortcuts import render, get_object_or_404
from courses.models import Course
from content.models import Content

# Create your views here.
def courses_main(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "home.html", context)

def one_course(request, id):
    course = get_object_or_404(Course, id=id)
    contents = Content.objects.filter(number = course.page)
    for content in contents:
        if content.course.id == course.id:
            link = content.link
    context = {
        "course": course,
        "course_link": link
    }
    return render(request, "detail.html", context)

def add_course(request):
    pass

def edit_course(request, id):
    pass