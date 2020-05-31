from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image
import random
import string
from curiousweb import settings

IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100

def resize_image(image_field, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, name=None, maintain_ratio = True):
    """
    Resizes an image from a Model.ImageField and returns a new image as a ContentFile
    """
    img = Image.open(image_field)
    hwratio =  img.size[1]/img.size[0]
    if width > height:
        new_img = img.resize((width, int(width * hwratio)))
    else:
        new_img = img.resize((int(height / hwratio), height))

    buffer = BytesIO()
    new_img.save(fp=buffer, format='JPEG')
    return ContentFile(buffer.getvalue())

#assuming your Model instance is called `instance`
def resize_image_field(image_field, width = IMAGE_WIDTH, height = IMAGE_HEIGHT):
    img_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '.jpg'
    img_path = settings.MEDIA_ROOT + img_name

    pillow_image = resize_image(
                      image_field,
                      width=width,
                      height=height,
                      name=img_path)

    image_field.save(img_name, InMemoryUploadedFile(
         pillow_image,       # file
         None,               # field_name
         img_name,           # file name
         'image/jpeg',       # content_type
         pillow_image.tell,  # size
         None)               # content_type_extra
    )
