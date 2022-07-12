from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    writer = models.CharField(max_length=20, null=True, blank=True, default="세은")
    feelings = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.title