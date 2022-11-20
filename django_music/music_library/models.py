from django.db import models
from datetime import date


class Artist(models.Model):
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(
        upload_to='music_library/artists',
        default='music_library/Blank.jpg',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.name


class Album(models.Model):
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    YEAR_CHOICES = [(year, year) for year in range(1900, date.today().year + 1)]

    name = models.CharField(max_length=100, verbose_name='Название')
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE, verbose_name='Исполнитель', related_name='albums')
    year = models.IntegerField(choices=YEAR_CHOICES, default=date.today().year, verbose_name='Год выпуска')
    image = models.ImageField(
        upload_to='music_library/albums',
        default='music_library/Blank.jpg',
        verbose_name='Изображение'
    )

    def __str__(self):
        return f'{self.year} {self.artist} - {self.name}'


class Track(models.Model):
    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    name = models.CharField(max_length=100, verbose_name='Название')
    track = models.FileField(upload_to='music_library/tracks', verbose_name='Трек')

    def __str__(self):
        return self.name


class TrackAlbum(models.Model):
    class Meta:
        verbose_name = 'Трек-альбом'
        verbose_name_plural = 'Треки-альбомы'

    album = models.ForeignKey(to=Album, on_delete=models.CASCADE, verbose_name='Альбом', related_name='tracks')
    track = models.ForeignKey(to=Track, on_delete=models.CASCADE, verbose_name='Трек', related_name='album')
    num = models.IntegerField(verbose_name='Номер трека в альбоме')

    def __str__(self):
        return f'{self.album} - {self.track}'
