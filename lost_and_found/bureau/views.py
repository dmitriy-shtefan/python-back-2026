from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import LostItemForm


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


def report_lost(request):
    form = LostItemForm()
    if request.method == "POST" and form.is_valid():
        form.save(commit=False)
        messages.success(request, "Повідомлення про загублену річ збережено.")
        return redirect("report_lost")

    return render(request, "bureau/report_lost.html", {"form": form})
