from django.db import models

class ScrapedData(models.Model):
    english_name = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.english_name} - {self.currency}"
		
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name