from django import forms
from django.conf import settings

from . import models

class MangaSeriesForm(forms.ModelForm):
    class Meta:
        model = models.MangaSeriesModel
        fields = ['name', 'author', 'description', 'volume_total', 'chapter_total']

class MangaVolumeForm(forms.Form):
    files = forms.FileField(label="Files", required=False, widget=forms.ClearableFileInput(attrs={'multiple': True, "accept": settings.MANGA_ACCEPTED_FORMATS}))
    @property
    def get_accepted_file_extensions(self):
        return settings.MANGA_ACCEPTED_FORMATS

    