from rest_framework import routers
from music_library.views import *


artist_router = routers.SimpleRouter()
album_router = routers.SimpleRouter()
track_router = routers.SimpleRouter()
artist_router.register(r'artist', ArtistViewSet)
artist_router.register(r'album', AlbumViewSet)
artist_router.register(r'track', TrackViewSet)
