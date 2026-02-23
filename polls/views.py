from django.http import HttpResponse  # type: ignore

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
