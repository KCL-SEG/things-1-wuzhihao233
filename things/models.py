from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)

class Thing(models.Model):

    name = models.CharField(max_length=30, unique = True)
    description = models.CharField(max_length = 120, unique = False, blank = True)
    quantity = models.PositiveSmallIntegerField(unique = False, validators=[MaxValueValidator(100), MinValueValidator(0)])