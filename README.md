# EXIF
Use the [CCD/CMOS dataset](https://github.com/alicevision/AliceVision/blob/develop/src/aliceVision/sensorDB/cameraSensors.db) from AliceVision to calculate the focal length.

## Typical Usage
```python
from EXIF.utils import focal_length_helper
focal_obtainer = focal_length_helper(img_path)
f = 0
try:
    f = focal_obtainer.obtain_focal_length_px(method='db')
except:
    f = focal_obtainer.obtain_focal_length_px(method='efl')
logging.info('f_exif = %f', (f))
return f
```

## Thanks
- https://github.com/alicevision/AliceVision
- https://pypi.org/project/exif/
- https://pypi.org/project/ExifRead/