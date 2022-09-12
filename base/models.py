from django.db import models

# Create your models here.


class ApiData(models.Model):
    filename = models.CharField(verbose_name="File Name",
                                max_length=200,)

    status = models.CharField(
        max_length=100, verbose_name="Status of the Process")

    createdby = models.CharField(
        max_length=100, verbose_name="Created By")

    assignedto = models.CharField(
        max_length=100, verbose_name="Assigned to the person")

    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename
