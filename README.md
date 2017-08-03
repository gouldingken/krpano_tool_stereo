# krpano_tool_stereo
A workflow for KRPano Tools (commercial product) to process VRay or GearVR panoramas.

Based on workflow outlined in this forum post https://krpano.com/forum/wbb/index.php?page=Thread&postID=69908

## Requirements

### Pillow
for image processing
```
$ pip install Pillow
```
http://pillow.readthedocs.io/en/3.0.x/installation.html

### KRPano Tools
KRPano Tools is required to be installed and registered.
http://krpano.com/download/

## Setup
`KRPANO_BASE_DIR` constant needs to point to the installation path for KRPano Tools (must be set in 2 files currently):
* run_kr_make_tour.py
* slices_to_sphere.py

## Basic Usage

### Generate Images
```
import process_all
process_all.run("C:\\VR-VIEW.jpg")
```

### Create Tour
```
from create_vtour import make_tour
make_tour('test_tour_1', [
    {'id': 'view_a', 'title': 'Entry Way', 'pano_folder': 'VR-VIEW-A'},
    {'id': 'view_b', 'title': 'Workspace', 'pano_folder': 'VR-VIEW-B'}
])
```
