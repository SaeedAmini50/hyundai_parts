from django.shortcuts import render
from django.http import HttpResponse


def home (requset):
    return HttpResponse("<h1> hello saeed amini </h1>")