# Camera calibration using OpenCV

## Dependencies
* [OpenCV](https://opencv.org/)

## Contents
* python script to automatically acquire images from a camera
* python script to extract camera intrinsics

## Running
To automatically acquire images with default parameters you can use:

    python record_images.py -d0 -n10 -p images/
    
To automatically calculate instrinsic camera parameters you can use:

    python extract_camera_intrinsics.py -p images/

## References
OpenCV Doc: [Camera Calibration](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html)
