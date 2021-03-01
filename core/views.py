from hashlib import md5

from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import ShorterIRLSerializer
from .models import URLInfo


class ShorterAPIView(APIView):
    serializer_class = ShorterIRLSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        url_info = URLInfo.objects.filter(full_url=serializer.validated_data.get('url'))
        if not url_info:

            url_info = URLInfo.objects.create(full_url=serializer.validated_data.get('url'),
                                              url_hash=md5(serializer.validated_data.get('url').encode()).hexdigest()[:10]
                                              )
        else:
            url_info = url_info.first()
        data = {
            "full_url": url_info.full_url,
            "hash_url": url_info.url_hash,
            "clicks": url_info.clicks
        }

        return Response(data, status=status.HTTP_200_OK)


class GetFullURLAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, url_hash, *args, **kwargs):
        url_info = URLInfo.objects.filter(url_hash=url_hash)
        if url_info:
            url_info = url_info.first()
            data = {
                "full_url": url_info.full_url,
                "hash_url": url_info.url_hash,
                "clicks": url_info.clicks
            }

            return Response(data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
