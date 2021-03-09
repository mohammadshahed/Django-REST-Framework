from django.shortcuts import (render, get_object_or_404, redirect)
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from DjangoRESTapp.models import Article
from DjangoRESTapp.serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import mixins
from rest_framework import generics


class GenericArticleView(generics.GenericAPIView, 
                            mixins.ListModelMixin, 
                            mixins.CreateModelMixin, 
                            mixins.UpdateModelMixin, 
                            mixins.RetrieveModelMixin, 
                            mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id=None):
        return self.destroy(request, id)


"""
class Articlelist(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article.html'

    def get(self, request):
        arti = Article.objects.all()
        serializer = ArticleSerializer(arti, many=True)
        return Response({'serializer':serializer.data, 'article': arti})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'articleDetails.html'

    def get_objects(self, id):
        try:
            return get_object_or_404(Article, id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        arti = self.get_objects(id)
        serializer = ArticleSerializer(arti)
        return Response(serializer.data)

    def post(self, request, id):
        arti = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(arti, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'article': arti})
        serializer.save()
        return redirect('article')

    def put(self, request, id):
        arti = self.get_objects(id)
        serializer = ArticleSerializer(arti, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        arti = self.get_objects(id)
        arti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

# @api_view(['GET', 'POST'])
# def articlelist(request):
#     if request.method == 'GET':
#         arti = Article.objects.all()
#         serializer = ArticleSerializer(arti, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def articledetails(request, pk):
#     try:
#         arti = Article.objects.get(pk=pk)
#     except arti.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'GET':
#         serializer = ArticleSerializer(arti)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = ArticleSerializer(arti, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         arti.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @csrf_exempt
# def article_list(request):
   
#     if request.method == 'GET':
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_detail(request, pk):
    
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)        