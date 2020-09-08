from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Todolist(models.Model):
    title = models.CharField(max_length = 250)
    content = models.TextField()
    created = models.DateField(default = timezone.now().strftime("%Y-%m-%d"))
    due = models.DateField(default = timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = "general")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
