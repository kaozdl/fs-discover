from django.db import models

# Create your models here.
class File(models.Model):

    path = models.CharField(max_length=32767, unique=True, db_index=True)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self) -> str:
        return f"{self.path}"

class Tag(models.Model):

    name = models.CharField(max_length=256)
    files = models.ManyToManyField('File')

    def __str__(self) -> str: 
        return f"{self.name}"

