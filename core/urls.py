from django.urls import path, include
from shorturl.utils.apps import get_api_url

from .views import (
    ShorterAPIView, GetFullURLAPIView
)

urlpatterns = [
    path(get_api_url(url_name='url-shorten'), ShorterAPIView.as_view(), name='api-url_shorten'),
    path(get_api_url(url_name='full-url/<str:url_hash>'), GetFullURLAPIView.as_view(), name='api-full_url')
]
