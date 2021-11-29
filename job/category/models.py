# from re import VERBOSE  #Читабельное название модели, в единственном числе
from django.db import models
from django.utils import timezone


class Work(models.Model):
    title = models.CharField(
        max_length = 50,
        verbose_name = "Title",
    )
    work_class = models.CharField(
        max_length = 50,
        verbose_name = "Class"
    )
    place = models.CharField(
        max_length = 30,
        verbose_name = "Place",
    )
    work_time = models.CharField(
        max_length = 10,
        verbose_name = "Busyness",
    )
    salary = models.CharField(
        max_length = 20,
        verbose_name = "Salary",
    )
    text = models.TextField(
        verbose_name = "Text",
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "work"
        verbose_name = "Work"
        verbose_name_plural = "Works"
