from django.db import models

class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

