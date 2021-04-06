from rest_framework import viewsets, permissions
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.BooksSerializer
  queryset = models.Books.objects.all()
  permission_classes = [permissions.AllowAny]