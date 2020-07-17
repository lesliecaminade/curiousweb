#PDF TO IMAGE CONVERSION
#IMPORT LIBRARIES
import pdf2image
from PIL import Image
import time
import curiousweb
import os
import string
import random
#DECLARE CONSTANTS


def save_images(pil_images):
    #This method helps in converting the images in PIL Image file format to the required image format
    index = 1
    OUTPUT_FOLDER = os.path.join(curiousweb.settings.MEDIA_ROOT,'handouts', 'handoutfile')
    filename = "page_" + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + ".jpg"
    full_path = os.path.join(OUTPUT_FOLDER, filename)
    for image in pil_images:
        image.save(full_path)
        index += 1

def pdftopil(input_path):
    #This method reads a pdf and converts it into a sequence of images
    #PDF_PATH sets the path to the PDF file
    #dpi parameter assists in adjusting the resolution of the image
    #output_folder parameter sets the path to the folder to which the PIL images can be stored (optional)
    #first_page parameter allows you to set a first page to be processed by pdftoppm
    #last_page parameter allows you to set a last page to be processed by pdftoppm
    #fmt parameter allows to set the format of pdftoppm conversion (PpmImageFile, TIFF)
    #thread_count parameter allows you to set how many thread will be used for conversion.
    #userpw parameter allows you to set a password to unlock the converted PDF
    #use_cropbox parameter allows you to use the crop box instead of the media box when converting
    #strict parameter allows you to catch pdftoppm syntax error with a custom type PDFSyntaxError

    PDF_PATH = input_path
    DPI = 200
    random_folder_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    OUTPUT_FOLDER = os.path.join(curiousweb.settings.MEDIA_ROOT,'handouts', 'temp')
    os.mkdir(OUTPUT_FOLDER)
    FIRST_PAGE = None
    LAST_PAGE = None
    FORMAT = 'jpg'
    THREAD_COUNT = 1
    USERPWD = None
    USE_CROPBOX = False
    STRICT = False

    start_time = time.time()
    pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
    print ("Time taken : " + str(time.time() - start_time))
    save_images(pil_images)
    return OUTPUT_FOLDER
