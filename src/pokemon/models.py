from django.db import models
from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=50, null=False, db_index=True, unique=True)
    details = models.JSONField()

    class Meta:
        db_table = 'pokemon'
        managed = True
