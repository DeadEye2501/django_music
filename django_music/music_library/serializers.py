from rest_framework import serializers
from .models import *


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('name', 'track')


class TracksAlbumSerializer(serializers.ModelSerializer):
    track = TrackSerializer()

    class Meta:
        model = TrackAlbum
        fields = ('track', 'num')


class TrackAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackAlbum
        fields = ('track', 'album', 'num')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('name', 'year', 'image', 'artist')


class AlbumsSerializer(serializers.ModelSerializer):
    tracks = TracksAlbumSerializer(many=True)

    class Meta:
        model = Album
        fields = ('name', 'year', 'image', 'tracks')


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumsSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('name', 'image', 'albums')


class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'image')
