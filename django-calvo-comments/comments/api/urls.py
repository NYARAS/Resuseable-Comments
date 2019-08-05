from django.conf.urls import url, include

from django.views.generic import TemplateView
from .views import CommentListAPIView, CommentCreateAPIView, CommentUpdateAPIView
# from .views import LoginUrlTestTemplateView
urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CommentUpdateAPIView.as_view(), name='update'),
  
]