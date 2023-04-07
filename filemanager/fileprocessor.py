from PIL import Image
from zipfile import ZipFile
from io import BytesIO

def validate_zip(file):
    try:
        with ZipFile(file, "r") as zip:
            if zip.testzip() == None:
                return True
    except:
        return False

def count_files(file):
    try:
        with ZipFile(file, "r") as zip:
            counter = 0
            for name in zip.infolist():
                if not name.is_dir():
                    counter = counter + 1

            return counter
    except:
        return 0
    

def generate_thumbnail(file):
    if not validate_zip(file): return False

    with ZipFile(file, "r") as zip:
        for file in zip.filelist:
            with zip.open(file, "r") as thumbnail:
                try:
                    img = Image.open(thumbnail)
                    blob = BytesIO()
                    img.save(blob, "JPEG")
                    return blob
                except Exception as e:
                    print(e)