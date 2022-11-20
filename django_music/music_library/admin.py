from django.contrib import admin
from .models import *


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist', 'image')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'track')


@admin.register(TrackAlbum)
class TrackAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'track', 'album')
