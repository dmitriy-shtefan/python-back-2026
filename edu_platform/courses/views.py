from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

LESSONS = {
    1: "HTTP",
    2: "Routing",
    3: "Views",
}

def index(request):
    context = {
        "name": "Kyrylo",
        "profile": {"group": "<b>P42</b>", "status": "active"},
        "courses": ["Python", "C#", "JavaScript", "Java"],
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



def course_list(request):
    return render(request, "course_list.html")


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
