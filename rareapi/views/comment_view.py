"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment, Author, Post

class CommentView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        author = Author.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data["post"])

        comment = Comment.objects.create(
            author = author,
            post = post,
            time_stamp = request.data["time_stamp"],
            content = request.data["content"]
        )
        serializer = CommentSerializer(comment)
        return Response(None, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.author = Author.objects.get(user=request.auth.user)
        comment.post = Post.objects.get(pk=request.data["post"])
        comment.time_stamp = request.data["time_stamp"]
        comment.content = request.data["content"]
        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'time_stamp', 'content')