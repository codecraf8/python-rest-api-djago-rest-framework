from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Note(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)])
