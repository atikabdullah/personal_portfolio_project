from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200,)
    date=models.DateField(auto_now=False, auto_now_add=False,)
    article=models.TextField()
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title
