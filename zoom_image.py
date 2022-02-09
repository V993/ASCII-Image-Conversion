from sys import argv
from PIL import Image

# if needed, zoom/crop into the image for greater detail.
def zoom_at(img, x, y, zoom):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)

in_image = Image.open(argv[1])
# zoomed_image = zoom_at(in_image)
zoomed_image.save("inverted"+argv[1], quality=95)