from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login;


def members(request):
    return HttpResponse("Hello Word")

