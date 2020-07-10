from django.db import models

class Url(models.Model):
    long_url = models.URLField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.long_url
