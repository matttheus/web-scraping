from django.db import models

class Scraping(models.Model):
    class Meta:
        db_table = 'Scraping'

    title = models.CharField(max_length=500, null=False, blank=False, unique=True)
    link = models.CharField(max_length=255, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title