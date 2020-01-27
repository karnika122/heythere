from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def index(request):

    # return HttpResponse("<marquee><h>welcome to my blog</h></marquee>")
    return render(request,"index.html")