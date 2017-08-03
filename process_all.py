import os

import mk_dirs
import vray_cube_to_krpano_slices
import combine_spheres
import slices_to_sphere
from os.path import basename


def run(image_path):
    dir_name = basename(image_path)
    dir_name = os.path.splitext(dir_name)[0]
    dir_name = dir_name.replace('.', '_')

    print('Processing: '+dir_name)

    mk_dirs.run(dir_name)

    print('Slicing: '+dir_name)
    # take the 12x1 image and slice into individual images with the correct names for KRPano
    vray_cube_to_krpano_slices.slice12(dir_name, image_path)

    # print('Making Sphericals: '+dir_name)
    # use KRPano to create equirectangular images from cube tiles
    # slices_to_sphere.run(dir_name)

    # print('Stacking Sphericals: '+dir_name)
    # stack the equirectangular images top and bottom for viewing in goggles
    # combine_spheres.run(dir_name)

    print('Completed: '+dir_name)
    print('-----------------------------------')

