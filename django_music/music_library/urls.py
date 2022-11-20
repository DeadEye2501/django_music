from django.urls import path, include
from music_library.routers import *


urlpatterns = [
    path('api/', include(artist_router.urls)),
    path('api/', include(album_router.urls)),
    path('api/', include(track_router.urls)),
]
