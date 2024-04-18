from django.shortcuts import render
from lessons.models import Lesson

def lesson_index(request):
    lessons = Lesson.objects.all()
    context = {
        "lessons": lessons
    }
    return render(request, "lessons/lesson_index.html", context)

def lesson_detail(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    context = {
        "lesson": lesson
    }
    return render(request, "lessons/lesson_detail.html",context)