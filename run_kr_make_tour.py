import subprocess
import logging
import os

# loosely based on https://github.com/manageyp/krpano_tool/blob/master/krpano.py

KRPANO_BASE_DIR = "C:\\app\\krpano-1.19-pr5"

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

# CONFIG = "templates\custom-vtour-normal.config"
CONFIG = "templates\\vtour-normal.config"

def _call_subprocess(cmd):
    try:
        out = subprocess.check_output(cmd, shell=True, cwd=KRPANO_BASE_DIR, stderr=subprocess.STDOUT).decode("utf-8")
        if out.lower().find('error') != -1:
            raise Exception(out)
    except subprocess.CalledProcessError as e:
        logging.error(e.output)
        raise
    else:
        logging.debug(out)


def _make_pano(images):

    preview_command = "krpanotools64.exe makepano -config=%s \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\"" % \
                      (CONFIG, images[0], images[1], images[2], images[3], images[4], images[5])
    _call_subprocess(preview_command)


def create_tour(dir_name):
    prefixes = {
        'right':'right.tiles',
        'left':'pano0001.tiles' # Not sure why "left" tiles are named pano0001 but it seems consistent
    }
    suffixes = [
        '_f',
        '_b',
        '_u',
        '_d',
        '_l',
        '_r'
    ]

    for prefix, value in prefixes.items():
        arr = []
        for stepNum in range(0, len(suffixes)):
            arr.append(os.path.join(THIS_DIR, dir_name, 'slices', prefix, prefix + suffixes[stepNum] + ".jpg"))

        _make_pano(arr) #calling this multiple times, adds panos to the panos folder

    return prefixes
