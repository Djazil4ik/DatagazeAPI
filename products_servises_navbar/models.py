from django.db import models

class Prod_Serv_Nav(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
