from django.shortcuts import render  # type: ignore
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('My Fav Movies')
def index(request):
    context = {'movies': ['rocky', 'jerry_2', 'gary_4']}
    return render(request, 'movies/index.html', context)
#


def about(request):
    return render(request, 'movies/about.html', {})


# app/templates/app/index.html
# movies/templates/movies/index.html
