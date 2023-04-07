from django import forms

from . import models

class MangaSeriesForm(forms.ModelForm):
    class Meta:
        model = models.MangaSeriesModel
        fields = ['name', 'author', 'description', 'volume_total', 'chapter_total']

class MangaVolumeForm(forms.Form):
    files = forms.FileField(label="Files", required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    