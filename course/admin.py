from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission
from django.contrib.admin import TabularInline, ModelAdmin


class ChoiceInline(TabularInline):
    model = Choice
    extra = 2


class QuestionInline(TabularInline):
    model = Question
    extra = 1


class LessonInline(TabularInline):
    model = Lesson
    extra = 1


class CourseAdmin(ModelAdmin):
    inlines = [LessonInline]


class LessonAdmin(ModelAdmin):
    inlines = [QuestionInline]


class QuestionAdmin(ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
