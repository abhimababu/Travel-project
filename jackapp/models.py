from django.db import models


# Create your models here.
class drink(models.Model):
    name = models.ImageField(upload_to='picture')
    desc = models.TextField()
    img = models.CharField(max_length=100)
# id: int
# name: str
# img: str
#  desc: str
