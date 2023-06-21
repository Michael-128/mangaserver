from sys import exit, argv
from PIL import Image

if len(argv) < 2:
    exit(1)

logo_name = argv[1]

logo = Image.open(logo_name)

logo.resize((1024, 1024)).save("./logo_1024.png")
logo.resize((512, 512)).save("./logo_512.png")
logo.resize((256, 256)).save("./logo_256.png")
logo.resize((128, 128)).save("./logo_128.png")
logo.resize((64, 64)).save("./logo_64.png")

