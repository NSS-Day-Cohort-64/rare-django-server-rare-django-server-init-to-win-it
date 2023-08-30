from django.db import models

class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE , related_name="created_posts")
    title = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category_posts")
    publication_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)
    tags = models.ManyToManyField("tag")
