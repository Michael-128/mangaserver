from django.shortcuts import render, redirect

from filemanager import models, forms, fileprocessor
from django.core.files.images import ImageFile

# Create your views here.
def dashboard(request):
    manga_series_models = models.MangaSeriesModel.objects.all()

    manga_series = []

    try:
        thumbnail = models.MangaVolumeModel.objects.select_related("manga_series").get(volume = 1, manga_series = model).thumbnail
    except:
        thumbnail = ""

    for model in manga_series_models:
        manga_series.append({
            'model': model,
            'thumbnail': thumbnail
        })

    return render(request, "dashboard.html", {'manga_series': manga_series})

def manga_details(request):
    if not 'name' in request.GET: return redirect("/")

    if request.method == "POST":
        manga_series_model = models.MangaSeriesModel.objects.get(name = request.GET["name"])
        files = request.FILES.getlist('files')
        print("post")
        if files:
            volume = models.MangaVolumeModel.objects.select_related("manga_series").filter(manga_series = manga_series_model).latest('volume').volume
            for file in files:
                volume = volume + 1
                if fileprocessor.validate_zip(file):
                    thumbnail = fileprocessor.generate_thumbnail(file)
                    #print(thumbnail)
                    manga_volume_model = models.MangaVolumeModel(file = file, thumbnail = ImageFile(thumbnail, name=f"thumbnail.jpg"), volume = volume, page_total = fileprocessor.count_files(file), manga_series = manga_series_model) 
                    manga_volume_model.save()


            #return redirect("/")

    print(request.GET['name'])
    manga = models.MangaSeriesModel.objects.get(name = request.GET["name"])
    print(manga)
    volumes = models.MangaVolumeModel.objects.select_related("manga_series").filter(manga_series = manga).all()

    return render(request, "manga_details.html", {'series': manga, 'volumes': volumes, 'form': forms.MangaVolumeForm()})