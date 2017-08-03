import subprocess
import logging
import os

# loosely based on https://github.com/manageyp/krpano_tool/blob/master/krpano.py

KRPANO_BASE_DIR = "C:\\app\\krpano-1.19-pr5"

CONVERT_CONFIG = "templates\\convertdroplets.config"

THIS_DIR = os.path.dirname(os.path.realpath(__file__))


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


def _generate_sphere(images, outFile):
    preview_command = "krpanotools64.exe cube2sphere -config=%s -o=\"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\"" % \
                      (CONVERT_CONFIG, outFile, images[0], images[1], images[2], images[3], images[4], images[5])
    _call_subprocess(preview_command)


def run(dir_name):
    prefixes = [
        'right',
        'left'
    ]
    suffixes = [
        '_f',
        '_b',
        '_u',
        '_d',
        '_l',
        '_r'
    ]

    for imNum in range(0, len(prefixes)):
        arr = []
        for stepNum in range(0, len(suffixes)):
            arr.append(os.path.join(THIS_DIR, dir_name, 'slices', prefixes[imNum], prefixes[imNum] + suffixes[stepNum] + ".jpg"))

        out_file = os.path.join(THIS_DIR, dir_name, 'spheres', 'sphere_{0}.jpg'.format(prefixes[imNum]))
        _generate_sphere(arr, out_file)
        print("generated sphere " + out_file)