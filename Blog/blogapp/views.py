from django.shortcuts import HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
# Create your views here.

class article_list(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class article_details(APIView):
    def get_object(self, id):
        try:
         return Article.objects.get(id=id)
        except Article.DoesNotExist:
         return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id):
       article = self.get_object(id)
       serializer = ArticleSerializer(article)
       return Response(serializer.data)
    
    def put(self, request, id):
        serializer = ArticleSerializer(self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
       article = self.get_object(id)
       article.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)