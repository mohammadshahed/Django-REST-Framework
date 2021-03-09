from django.urls import path
# from DjangoRESTapp.views import  Articlelist, ArticleDetails
from DjangoRESTapp.views import  GenericArticleView

urlpatterns = [
    # path('article_list/', article_list, name='article_list'),
    # path('article_detail/<int:pk>/', article_detail, name='article_detail'),
    # path('articlelist/', Articlelist.as_view(), name='articlelist'),
    # path('articledetails/<int:id>/', ArticleDetails.as_view(), name='articledetails'),
    # path('articleadd/', Actileformview, name='articleform'),
    path('generic/article/', GenericArticleView.as_view(), name='genericarticle'),
    path('generic/article/<int:id>/', GenericArticleView.as_view(), name='genericarticle'),
    # path('viewsets/', include(router.urls)),
    # path('viewsets/<int:pk>/', include(router.urls))
]