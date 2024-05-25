from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    body_text = models.TextField()
    image = models.ImageField()
    date = models.DateField()
    URL = models.URLField()

    def __str__(self) -> str:
        return self.title
    
