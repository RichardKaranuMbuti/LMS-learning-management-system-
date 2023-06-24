from django.db import models

class Department(models.Model):
    code = models.CharField('Department Code', max_length=20, primary_key=True)
    name = models.CharField('Department Name', max_length=100)
    description = models.TextField('Department Description')

    def __str__(self):
        return self.name


class Unit(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    code = models.CharField('Unit Code', max_length=20, primary_key=True)
    name = models.CharField('Unit Name', max_length=100)
    description = models.TextField('Unit Description')

    def __str__(self):
        return self.name
