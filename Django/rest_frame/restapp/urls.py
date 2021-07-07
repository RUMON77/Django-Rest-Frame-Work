from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static
#from restapp.views import GenericArticleView
from rest_framework.routers import DefaultRouter
#router = DefaultRouter()
#router.register(r'article', GenericArticleView, basename='article')


from restapp.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')



urlpatterns = [
    path('article/', views.ArticleList.as_view()),
    path('article/<int:pk>/', views.ArticleDetail.as_view()),
    #path('generic/article/', GenericArticleView.as_view(), name="genericarticle"),
    #path('generic/article/<int:id>/', GenericArticleView.as_view(), name="genericarticle"),
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:pk>/', include(router.urls)),
]



"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
"""
