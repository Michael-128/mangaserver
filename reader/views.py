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

    return render(request, 'reader.html', {'file': manga_volume.file, 'page_total': manga_volume.page_total, 'page_current': manga_volume.page_current})

def get_image(request):
    if not request.GET["file"]: return HttpResponse({})

    volume = models.MangaVolumeModel.objects.get(file = request.GET["file"])
    page = 1
    
    if not request.GET["page"]: 
        page = volume.page_current
    else:
        page = request.GET["page"]
        volume.page_current = request.GET["page"]
        volume.save()
    
    print(page)

    with ZipFile(f"media/{request.GET['file']}", 'r') as zip:
        filelist = zip.namelist()
        filelist.sort()

        index = int(page) - 1

        k = 0
        while filelist[k][-1] == "/":
            filelist.reverse()
            filelist.pop()
            filelist.reverse()
            k = k + 1

        #print(filelist)

        file = zip.read(filelist[index])
        return HttpResponse(file, content_type="image/jpeg")