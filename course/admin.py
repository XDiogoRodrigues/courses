from django.contrib import admin

from .models import Course, Coment, Section

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'quantity_classes', 'price', 'name_teacher', 'level', 'assessments', 'quantity_assessment')


@admin.register(Coment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ('coment',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)