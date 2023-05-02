from django.db import models


class Task(models.Model):
    title = models.CharField("عنوان", max_length=200)
    done = models.BooleanField("انجام شده")

    class Meta:
        verbose_name = "تسک"
        verbose_name_plural = "تسک ها"

    def __str__(self):
        return self.title
