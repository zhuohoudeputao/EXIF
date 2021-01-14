import os
from utils import *
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
import matplotlib.pyplot as plt

def test_obtain_exif():
    img_path = os.path.join(get_path(), 'data/清晖园-黄玉秋/微信图片_20191223163306.jpg')
    fl, efl, img_width_px, img_height_px, make, model = focal_length_helper.obtain_exif_exif(img_path)
    print(fl, efl, img_width_px, img_height_px,  make, model)
    assert type(make)==str
    assert type(model)==str

def test_obtain_fl():
    img_path = os.path.join(get_path(), 'data/清晖园-黄玉秋/微信图片_20191223163306.jpg')
    fl_px_1 = focal_length_helper(img_path).obtain_focal_length_px(method='db')
    fl_px_2 = focal_length_helper(img_path).obtain_focal_length_px(method='efl')
    print(fl_px_1)
    print(fl_px_2)
    assert abs(fl_px_1 - fl_px_2) < 100

def test_obtain_matrix():
    img_path = os.path.join(get_path(), 'data/清晖园-黄玉秋/微信图片_20191223163306.jpg')
    k_1 = focal_length_helper(img_path).obtain_intrinsic_matrix(method='db')
    k_2 = focal_length_helper(img_path).obtain_intrinsic_matrix(method='efl')
    print(k_1)
    print(k_2)

def test_extract():
    # paths = ['data/东莞可园-顾雪萍',
    #         'data/余荫山房-林祖轩',
    #         'data/其他照片/照片',
    #         'data/开平立园地面照片',
    #         'data/清晖园-黄玉秋']
    paths = ['data/其他照片/照片']
    for path in paths:
        df_db = focal_length_helper.extract_intrinsics_df(os.path.join(get_path(), path), method='db')
        df_efl = focal_length_helper.extract_intrinsics_df(os.path.join(get_path(), path), method='efl')
        df = pd.concat([df_db['fl_px'], df_efl['fl_px']], axis=1)
        df.columns = ['db', 'efl']
        # print(df)
        plt.figure(dpi=600)
        df.plot.hist(alpha=0.2)
        plt.title(path)
        plt.xlabel('Focal Length (px)')
        plt.show()
# %%
# test_obtain_exif()
# test_obtain_fl()
# test_obtain_matrix()
test_extract()
# %%
