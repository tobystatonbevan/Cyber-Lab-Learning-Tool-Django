from django.shortcuts import render

def lesson_index(request):
    return render(request, "lessons/lesson_index.html",{})