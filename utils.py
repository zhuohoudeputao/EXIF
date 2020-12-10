import os
import exifread
import pandas as pd
import numpy as np

def obtain_intrinsics(file_path):
    '''Obtain the intrinsics of a photo from exif information.

    Attributes:
        file_path: the absolute path of the photo
    
    Returns:
        f_x: focal length on x dimension (pixles)
        f_y: focal length on y dimension (pixels)
        x_0: shift on x dimension (pixels)
        y_0: shift on y dimension (pixels)
    '''
    with open(file_path, 'rb') as image_file:
        tags = exifread.process_file(image_file, details=False)
        # print(tags.keys())
        if 'EXIF FocalLength' in tags.keys():
            raise AttributeError('Focal Length is missing in exif')

        focal_length = tags['EXIF FocalLength'].values[0].num / tags['EXIF FocalLength'].values[0].den
        pixel_x_dimension = tags['EXIF ExifImageWidth'].values[0]
        pixel_y_dimension = tags['EXIF ExifImageLength'].values[0]
        x_resolution = tags['Image XResolution'].values[0].num
        y_resolution = tags['Image YResolution'].values[0].num

        f_x = focal_length / (25.4 / x_resolution)
        f_y = focal_length / (25.4 / y_resolution)
        x_0 = pixel_x_dimension/2
        y_0 = pixel_y_dimension/2
        # print('focal length =', focal_length, 'mm')
        # print('image width =', pixel_x_dimension, 'pixels')
        # print('image height =', pixel_y_dimension, 'pixels')
        # print('x_resolution =', x_resolution, 'dpi')
        # print('y_resolution =', y_resolution, 'dpi')
        # print('f_x =', f_x, 'pixels')
        # print('f_y =', f_y, 'pixels')
        # print('x_0 =', x_0, 'pixels')
        # print('y_0 =', y_0, 'pixels')
        return f_x, f_y, x_0, y_0

def obtain_intrinsic_matrix(file_path):
    '''Obtain the intrinsic_matrix of a photo.

    Attributes:
        file_path: the absolute path of the photo
    
    Returns:
        K: an intrinsic matrix in numpy
    '''
    f_x, f_y, x_0, y_0 = obtain_intrinsics(file_path)
    intrinsic_matrix = [[f_x, 0, x_0], [0, f_y, y_0], [0, 0, 1]]
    # print('K = ', intrinsic_matrix)
    return np.mat(intrinsic_matrix)

def extract_intrinsic(data_paths):
    '''Extract the intrinsic matrix of photos in the data_paths. 

    Attributes:
        data_path: the absolute path of photos
    
    Returns:
        A pands dataframe contains the pairs of filename and intrinsics
    '''
    df = pd.DataFrame(columns=['f_x', 'f_y', 'x_0', 'y_0'], dtype=np.float16)
    index = 0
    for data_path in data_paths:
        for filename in os.listdir(data_path):
            file_path = os.path.join(data_path, filename)
            # print(file_path)
            try:
                intrinsics = obtain_intrinsics(file_path)
                df.loc[index] = intrinsics
                index += 1
            except AssertionError as e:
                continue
        
    # print(df)
    return df

df = extract_intrinsic(['D:\lzx_work\EXIF\东莞可园-顾雪萍'])
# df.loc[:, ['f_x','f_y']].plot()
df.f_x.value_counts()
df.f_x.plot.kde()