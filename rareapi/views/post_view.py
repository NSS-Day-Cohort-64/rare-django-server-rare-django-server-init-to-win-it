"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, Author, Category, Tag, Comment

class PostView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        print(request.data)
        author = Author.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["category"])
        tags = Tag.objects.filter(pk__in=request.data["tags"])

        post = Post.objects.create(
            author = author,
            title = request.data["title"],
            category = category,
            content = request.data["content"]
        )
        
        post.tags.set(tags)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.category = Category.objects.get(pk=request.data["category"])
        post.content = request.data["content"]
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('label' ,)

class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('full_name' ,)

class CommentSerializer(serializers.ModelSerializer):
    author = AuthorPostSerializer(many=False)
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'time_stamp', 'content')

class PostSerializer(serializers.ModelSerializer):
    author = AuthorPostSerializer(many=False)
    category = CategoryPostSerializer(many=False)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'category', 'publication_date', 'content', 'comments')
