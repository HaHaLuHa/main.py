"""
读入一个图片，切成指定数目个小图片(16个)

"""
import os
from PIL import Image
import tifffile as tiff
import numpy as np


cut_num = 5  # 4*4=16个图片


# 将图片填充为正方形
def fill_image(image):
    width, height = image.size
    # 选取长和宽中较大值作为新图片的
    new_image_length = width if width > height else height
    # 生成新图片[白底]
    # new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
    new_image = Image.new(image.mode, (new_image_length, new_image_length))
    # 将之前的图粘贴在新图上，居中
    if width > height:  # 原图宽大于高，则填充图片的竖直维度
        # (x,y)二元组表示粘贴上图相对下图的起始位置
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))
    return new_image


# 切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / cut_num)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0, cut_num):  # 两重循环，生成图片基于原图的位置
        for j in range(0, cut_num):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    return image_list


# 保存
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('out/' + str(index) + '.tif')
        index += 1


if __name__ == '__main__':
    file_path = "C:/Users/lc/Desktop/pic/T01_1.tif"
    image = tiff.imread(file_path)
    print(image.shape)
    # os.mkdir("out")
    image = Image.open(file_path)
    # image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)

# '''
# 将指定文件夹里面的图片拼接成一个大图片
# '''
# import PIL.Image as Image
# import os
#
# IMAGES_PATH = 'out\\'  # 图片集地址
# IMAGES_FORMAT = ['.bmp', '.BMP']  # 图片格式
# IMAGE_SIZE = 2048  # 每张小图片的大小
# IMAGE_ROW = 4  # 图片间隔，也就是合并成一张图后，一共有几行
# IMAGE_COLUMN = 4  # 图片间隔，也就是合并成一张图后，一共有几列
# IMAGE_SAVE_PATH = 'final.bmp'  # 图片转换后的地址
#
# # 获取图片集地址下的所有图片名称
# image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
#                os.path.splitext(name)[1] == item]
#
# # 简单的对于参数的设定和实际图片集的大小进行数量判断
# if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
#     raise ValueError("合成图片的参数和要求的数量不能匹配！")
#
#
# # 定义图像拼接函数
# def image_compose():
#     to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # 创建一个新图
#     # 循环遍历，把每张图片按顺序粘贴到对应位置上
#     for y in range(1, IMAGE_ROW + 1):
#         for x in range(1, IMAGE_COLUMN + 1):
#             from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
#                 (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
#             to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
#     to_image = to_image.convert('L')
#     return to_image.save(IMAGE_SAVE_PATH)  # 保存新图
#
#
# image_compose()  # 调用函数