import os
from PIL import Image


def _ensureDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def slice12(dir_name, image_path):
    # VRay output is comprised of 12 images 6 right eye and 6 left eye
    # https://ggnome.com/forum/viewtopic.php?t=11005
    # https://krpano.com/forum/wbb/index.php?page=Thread&postID=69908
    prefixes = [
        'left',
        'right'
    ]
    suffixes = [
        '_r',
        '_l',
        '_u',
        '_d',
        '_b',
        '_f'
    ]

    # Rotate DOWN image 90 deg Left (90 deg CCW)
    # Rotate UP image 90 deg Right (90 deg CW)
    # rotations = {
    #     '_d': 90,
    #     '_u': -90
    # }

    # Front, Back, Left, Right → Flip horizontally
    # Up, Down → Flip vertically

    flip = {
        '_r': Image.FLIP_LEFT_RIGHT,
        '_l': Image.FLIP_LEFT_RIGHT,
        '_b': Image.FLIP_LEFT_RIGHT,
        '_f': Image.FLIP_LEFT_RIGHT,
        '_d': Image.FLIP_TOP_BOTTOM,
        '_u': Image.FLIP_TOP_BOTTOM
    }

    im = Image.open(image_path)

    step = im.height

    w = step * 12
    h = step

    for imNum in range(0, len(prefixes)):
        slices = len(suffixes)
        for stepNum in range(0, slices):
            x = imNum * step * slices + stepNum * step
            mx = min(x + step, w)
            my = min(step, h)

            buffer = Image.new("RGB", [step, step], (255, 255, 255))
            tile = im.crop((x, 0, mx, my))

            suffix = suffixes[stepNum]
            # if suffix in rotations:
            #     tile = tile.rotate(rotations[suffix])

            tile = tile.transpose(flip[suffix])

            buffer.paste(tile, (0, 0))

            _ensureDir(os.path.join(dir_name, 'slices', prefixes[imNum]))

            out_file = os.path.join(dir_name, 'slices', prefixes[imNum], prefixes[imNum] + suffix + '.jpg')
            buffer.save(out_file, "JPEG")
            print(out_file)
