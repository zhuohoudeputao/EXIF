# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Obtain camera intrinsic from exif information
# ## Focal length $f$
# $Focal~length~(pixel) = \frac{Focal~length~(mm)}{25.4mm/resolution~(dpi)}$
# 
# ## Offsets $x_0, y_0$
# $x_0=\frac{image~width~(pixel)}{2}, ~y_0=\frac{image~height~(pixel)}{2}$

# %%
get_ipython().system('pip install exif')
get_ipython().system('conda install -c conda-forge exifread')


# %%
from exif import Image
with open('D:\lzx_work\EXIF\开平立园地面照片\DSC02828.JPG', 'rb') as image_file:
    image = Image(image_file)
    if image.has_exif:
        # print(dir(image))
        print('focal length =', image.focal_length, 'mm')
        print('image width =', image.pixel_x_dimension, 'pixels')
        print('image height =', image.pixel_y_dimension, 'pixels')
        print('x_resolution =', image.x_resolution, 'dpi')
        print('y_resolution =', image.y_resolution, 'dpi')
        dx = 25.4/image.x_resolution
        dy = 25.4/image.y_resolution
        print('dx =', dx, 'mm')
        print('dy =', dy, 'mm')
        f_x = image.focal_length/dx
        f_y = image.focal_length/dy
        print('f_x =', f_x, 'pixels')
        print('f_y =', f_y, 'pixels')
        x_0 = image.pixel_x_dimension/2
        y_0 = image.pixel_y_dimension/2
        print('x_0 =', x_0, 'pixels')
        print('y_0 =', y_0, 'pixels')
        K = [[f_x, 0, x_0], [0, f_y, y_0], [0, 0, 1]]
        print('K = ', K)


# %%
import exifread
# from Pillow import Image
with open('D:\lzx_work\EXIF\开平立园地面照片\DSC02828.JPG', 'rb') as image_file:
    tags = exifread.process_file(image_file, details=False)
    # print(tags.keys())
    focal_length = tags['EXIF FocalLength'].values[0].num/tags['EXIF FocalLength'].values[0].den
    pixel_x_dimension = tags['EXIF ExifImageWidth'].values[0]
    pixel_y_dimension = tags['EXIF ExifImageLength'].values[0]
    x_resolution = tags['Image XResolution'].values[0].num
    y_resolution = tags['Image YResolution'].values[0].num
    dx = 25.4/x_resolution
    dy = 25.4/y_resolution
    f_x = focal_length/dx
    f_y = focal_length/dy
    x_0 = pixel_x_dimension/2
    y_0 = pixel_y_dimension/2
    print('focal length =', focal_length, 'mm')
    print('image width =', pixel_x_dimension, 'pixels')
    print('image height =', pixel_y_dimension, 'pixels')
    print('x_resolution =', x_resolution, 'dpi')
    print('y_resolution =', y_resolution, 'dpi')
    print('dx =', dx, 'mm')
    print('dy =', dy, 'mm')
    print('f_x =', f_x, 'pixels')
    print('f_y =', f_y, 'pixels')
    print('x_0 =', x_0, 'pixels')
    print('y_0 =', y_0, 'pixels')
    intrinsic_matrix = [[f_x, 0, x_0], [0, f_y, y_0], [0, 0, 1]]
    print('K = ', intrinsic_matrix)


# %%



