import os
import pystache
import shutil, errno
import run_kr_make_tour

def copy_anything(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    try:
        shutil.copytree(src, dst)
    except OSError as exc:  # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


def generate_xml(scenes, tour_name):
    renderer = pystache.Renderer()
    content = renderer.render_path('tours/' + tour_name + '/tour.xml.mustache', {'scenes': scenes})
    os.remove('tours/' + tour_name + '/tour.xml.mustache')
    os.remove('tours/' + tour_name + '/tour.xml')
    f = open('tours/' + tour_name + '/tour.xml', 'w', encoding='utf-8')
    f.write(content)
    f.close()


def make_tour(tour_name, scenes):
    copy_anything('templates/vtour', 'tours/' + tour_name)
    for scene in scenes:
        panos = run_kr_make_tour.create_tour(scene['pano_folder'])

        for prefix, value in panos.items():
            src = os.path.join(scene['pano_folder'], 'slices', prefix, 'vtour', 'panos', value)
            dst = os.path.join('tours', tour_name, 'panos', scene['id'] + '_stereo_' + prefix.upper()[0])

            copy_anything(src, dst)
            shutil.rmtree(os.path.join(scene['pano_folder'], 'slices', prefix, 'vtour'))

    generate_xml(scenes, tour_name)


make_tour('test_tour_1', [
    {'id': 'view_a', 'title': 'Entry Way', 'pano_folder': 'VR-VIEW-A_denoiser'},
    {'id': 'view_b', 'title': 'Workspace', 'pano_folder': 'VR-VIEW-A_Alpha'}
])
