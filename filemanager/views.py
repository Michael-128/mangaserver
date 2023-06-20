from django.shortcuts import render, redirect
from . import forms
from . import models

from .fileprocessor import generate_thumbnail, validate_zip, count_files

from django.core.files.images import ImageFile

# Create your views here.
def add_manga_series(request):
    if request.method == "POST":
        manga_series_model = models.MangaSeriesModel()
        form = forms.MangaSeriesForm(request.POST, instance=manga_series_model)
        files = request.FILES.getlist('files')
        if form.is_valid():
            manga_series_model.save()
            if files:
                volume = 0
                for file in files:
                    volume = volume + 1
                    if validate_zip(file):
                        thumbnail = generate_thumbnail(file)
                        #print(thumbnail)
                        manga_volume_model = models.MangaVolumeModel(file = file, thumbnail = ImageFile(thumbnail, name=f"thumbnail.jpg"), volume = volume, page_total = count_files(file), manga_series = manga_series_model) 
                        manga_volume_model.save()


            return redirect("/")

    return render(request, "add_manga_series.html", {'manga_series_form': forms.MangaSeriesForm(), 'manga_volume_form': forms.MangaVolumeForm()})