from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from zipfile import ZipFile
from PIL import Image
from io import BytesIO

from filemanager import models

# Create your views here.
def reader(request):
    manga = models.MangaSeriesModel.objects.get(name = request.GET["name"])
    manga_volume = models.MangaVolumeModel.objects.select_related('manga_series').get(volume = request.GET["volume"], manga_series = manga)

    return render(request, 'reader.html', {'file': manga_volume.file, 'page_total': manga_volume.page_total})

def get_image(request):
    if not request.GET["file"] or not request.GET["page"]: return HttpResponse({})

    with ZipFile(f"media/{request.GET['file']}", 'r') as zip:
        filelist = zip.namelist()
        filelist.sort()

        index = int(request.GET['page']) - 1

        k = 0
        while filelist[k][-1] == "/":
            filelist.reverse()
            filelist.pop()
            filelist.reverse()
            k = k + 1

        print(filelist)

        file = zip.read(filelist[index])
        return HttpResponse(file, content_type="image/jpeg")