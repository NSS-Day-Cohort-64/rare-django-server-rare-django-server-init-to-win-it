from django.db import models

class Comment(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="written_comments")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    time_stamp = models.DateTimeField(auto_now_add=True)    
    content = models.CharField(max_length=255)
