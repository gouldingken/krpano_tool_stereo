import os


def _ensureDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def run(dir):
    _ensureDir(dir)
    _ensureDir(dir+'/slices')
    _ensureDir(dir+'/spheres')
    _ensureDir(dir+'/stacked')
