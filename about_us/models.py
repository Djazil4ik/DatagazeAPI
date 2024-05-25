from django.db import models

class About_Us(models.Model):
    title = models.CharField(max_length=255)
    body_text = models.TextField()

    def __str__(self) -> str:
        return self.title

class Our_Certificate(models.Model):
    title = models.CharField(max_length=255)
    cetificate = models.ImageField()

    def __str__(self) -> str:
        return self.title
    
class Company_License(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    license = models.ImageField()

    def __str__(self) -> str:
        return self.title
    
