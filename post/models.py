from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    preview = models.TextField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')  # 'images/' is the upload path, you can change it

    def __str__(self):
        return self.title
