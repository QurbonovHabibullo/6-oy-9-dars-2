from django import forms
from .models import Course, Lesson

# Course formasi
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

# Lesson formasi
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']
