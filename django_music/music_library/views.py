from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *


class ArtistPagination(PageNumberPagination):
    page_size = 12


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer
    pagination_class = ArtistPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ArtistSerializer(instance)
        return Response(serializer.data)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        track_data = {'name': request.data.get('name'), 'track': request.data.get('track')}
        album_data = {'album': request.data.get('album'), 'num': request.data.get('num')}

        serializer = self.get_serializer(data=track_data)
        serializer.is_valid(raise_exception=True)
        track = serializer.save()

        album_data['track'] = track.pk
        serializer2 = TrackAlbumSerializer(data=album_data)
        serializer2.is_valid(raise_exception=True)
        serializer2.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
