from django.shortcuts import render


def home(request):
    return render(request, "bureau/home.html")


def found(request):
    items = [
        {
            "name": "Синя парасолька",
            "place": "Гардероб",
            "date": "09.11.2026",
        },
        {
            "name": "Чорні навушники",
            "place": "Кабінет 204",
            "date": "06.11.2026",
        },
        {
            "name": "Зелена пляшка для води",
            "place": "Спортивна зала",
            "date": "05.11.2026",
        },
    ]
    return render(request, "bureau/found.html", {"items": items})


def pickup(request):
    return render(request, "bureau/pickup.html")
