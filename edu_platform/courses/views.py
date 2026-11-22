from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Course

LESSONS = {
    1: "HTTP",
    2: "Routing",
    3: "Views",
}

def index(request):
    courses = Course.objects.filter(is_active=True)
    context = {
        "name": "Kyrylo",
        "profile": {"group": "<b>P42</b>", "status": "active"},
        "courses": courses,
    }

    return render(request, "index.html", context)


def profile(request):
    context = {
        "username": "KYRYLO",
        "balance": 1234.5,
        'joined': datetime.now(),
        'bio': 'Люблю Python...'
    }

    # comment

    return render(request, "profile.html", context)



def courses_list(request):
    courses = Course.objects.all()

    return render(request, "course_list.html", {"courses": courses})


def course_details(request, pk):
    course = get_object_or_404(Course, id=pk)

    return render(request, "course_details.html", {"course": course})


def contacts(request):
    return HttpResponse("Контакти навчальної платформи")


def lesson_detail(request, lesson_id):
    lesson = LESSONS.get(lesson_id)
    if lesson is None:
        return HttpResponse("Урок не знайдено", status=404)
    return HttpResponse(f"<h1>Урок {lesson_id}: {lesson}</h1>")


def course_100(request):
    number = request.GET.get("n", "0")
    return HttpResponse(
        f"Hello Django!<br/>Course is 100!<br/>"
        f"Method: {request.method}<br/>GET param: {number}"
    )

def old_contacts(request):
    return HttpResponseRedirect("/contacts/")
