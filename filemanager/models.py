from django.db import models


# Create your models here.
class MangaSeriesModel(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    
    volume_total = models.IntegerField(verbose_name="Total Volumes", null=True, blank=True)
    chapter_total = models.IntegerField(verbose_name="Total Chapters", null=True, blank=True)

    @property
    def thumbnail(self):
        related_volume = MangaVolumeModel.objects.select_related("manga_series").filter(manga_series = self).get(volume = 1)
        return related_volume.thumbnail

    def __str__(self):
        if self.author:
            return f"[{self.author}] {self.name}"
        
        return self.name
    
class MangaVolumeModel(models.Model):
    file = models.FileField()
    @property
    def file_size(self):
        return self.file.size

    thumbnail = models.ImageField(null=True)

    volume = models.IntegerField(null=True)
    chapter = models.IntegerField(null=True)

    page_total = models.IntegerField(verbose_name="Total Pages")
    page_current = models.IntegerField(default=1)

    manga_series = models.ForeignKey(MangaSeriesModel, on_delete=models.CASCADE)

    @property
    def progress(self):
        return round((self.page_current/self.page_total)*100)

    def __str__(self):
        return f"{self.manga_series.name} Vol. {self.volume}"

    class Meta:
        ordering = ['volume']