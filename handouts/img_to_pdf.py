import img2pdf
import os
import curiousweb
import random
import string

def convert(input_path):
    # convert all files ending in .jpg inside a directory
    dirname = input_path
    save_path = os.path.join(curiousweb.settings.MEDIA_ROOT, 'handouts', 'handoutfile')
    random_pdf_name = 'temp_' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '.pdf'
    full_path = os.path.join(save_path, random_pdf_name)
    with open(full_path,"wb") as f:
        imgs = []
        for fname in os.listdir(dirname):
            if not fname.lower().endswith(('.jpg', '.jpeg')):
                continue
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(img2pdf.convert(imgs))

    return full_path
