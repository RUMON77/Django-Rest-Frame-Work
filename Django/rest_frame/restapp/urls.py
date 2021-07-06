from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static
from restapp.views import GenericArticleView

urlpatterns = [
    path('article/', views.ArticleList.as_view()),
    path('article/<int:pk>/', views.ArticleDetail.as_view()),
    path('generic/article/', GenericArticleView.as_view(), name="genericarticle"),
    path('generic/article/<int:id>/', GenericArticleView.as_view(), name="genericarticle"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
"""