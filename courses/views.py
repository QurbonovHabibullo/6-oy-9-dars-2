from django.shortcuts import render, get_object_or_404,redirect
from .models import Course, Lesson
from .forms import CourseForm, LessonForm
# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

def create_lesson(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course  
            lesson.save()
            return redirect('course_detail', pk=course.id)  
    else:
        form = LessonForm()
    return render(request, 'courses/create_lesson.htm', {'form': form, 'course': course})