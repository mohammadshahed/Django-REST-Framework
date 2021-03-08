from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from DjangoRESTapp.models import Article
from DjangoRESTapp.serializers import ArticleSerializer

@csrf_exempt
def articlelist(request):
   
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)