from PIL import Image
import os


def run(dir_name):
    prefixes = [
        'right',
        'left'
    ]

    for imNum in range(0, len(prefixes)):
        im = Image.open(os.path.join(dir_name, 'spheres', 'sphere_{0}.jpg'.format(prefixes[imNum])))
        if imNum == 0:
            buffer = Image.new("RGB", [im.width, im.width], (255, 255, 255))

        buffer.paste(im, (0, imNum * im.height))
        buffer.save(os.path.join(dir_name, 'stacked', 'stereo.jpg'), "JPEG")
