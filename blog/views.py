from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def hi_shredder(request):
    return JsonResponse({"key": "Hi", "value": "Shredder"})