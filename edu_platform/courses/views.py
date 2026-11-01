from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def course_details(request, pk):
    return HttpResponse(f"<h1>{request.GET.get('a', 'dsdddd')}</h1>")