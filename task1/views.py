from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def send_json(request):
    data = {"slackUsername": "Mastermind",
            "backend": True, "age": 22,
            "bio": "I am an up and coming Django backend developer."}

    return JsonResponse(data)
