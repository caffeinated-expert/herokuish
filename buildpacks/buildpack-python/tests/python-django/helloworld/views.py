import os

from django.http import HttpResponse


def home(request):
    return HttpResponse("Powered by Deis\n")
