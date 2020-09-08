from django.contrib import admin
from . import models

class TodolistAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "due")
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.Todolist, TodolistAdmin)
admin.site.register(models.Category, CategoryAdmin)
