from django.db import models

# Create your models here.


class Tasks(models.Model):
    Task_Title = models.CharField(max_length=80)
    Completed = models.BooleanField(default=False)
    Creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Task_Title