
from cv2 import cv2
import numpy as np
import os

# 分割后的图片的文件夹，以及拼接后要保存的文件夹
pic_path = '/result/'
pic_target = 'picture/'
# 数组保存分割后图片的列数和行数，注意分割后图片的格式为x_x.jpg，x从1开始
num_width_list = []
num_lenght_list = []
# 读取文件夹下所有图片的名称
picture_names = os.listdir(pic_path)
if len(picture_names) == 0:
    print("没有文件")

else:
    # 获取分割后图片的尺寸
    img_1_1 = cv2.imread(pic_path + '1_1.jpg')
    (width, length, depth) = img_1_1.shape
    # 分割名字获得行数和列数，通过数组保存分割后图片的列数和行数
    for picture_name in picture_names:
        num_width_list.append(int(picture_name.split("_")[0]))
        num_lenght_list.append(int((picture_name.split("_")[-1]).split(".")[0]))
    # 取其中的最大值
    num_width = max(num_width_list)
    num_length = max(num_lenght_list)
    # 预生成拼接后的图片
    splicing_pic = np.zeros((num_width * width, num_length * length, depth))
    # 循环复制
    for i in range(1, num_width + 1):
        for j in range(1, num_length + 1):
            img_part = cv2.imread(pic_path + '{}_{}.jpg'.format(i, j))
            splicing_pic[width * (i - 1): width * i, length * (j - 1): length * j, :] = img_part
    # 保存图片，大功告成
    cv2.imwrite(pic_target + 'result.jpg', splicing_pic)
    print("done!!!")

# import cv2
# img = cv2.imread("11.tif",1)
# #第二个参数是通道数和位深的参数，
# #IMREAD_UNCHANGED = -1#不进行转化，比如保存为了16位的图片，读取出来仍然为16位。
# #IMREAD_GRAYSCALE = 0#进行转化为灰度图，比如保存为了16位的图片，读取出来为8位，类型为CV_8UC1。
# #IMREAD_COLOR = 1#进行转化为RGB三通道图像，图像深度转为8位
# #IMREAD_ANYDEPTH = 2#保持图像深度不变，进行转化为灰度图。
# #IMREAD_ANYCOLOR = 4#若图像通道数小于等于3，则保持原通道数不变；若通道数大于3则只取取前三个通道。图像深度转为8位
# print (img)
# print (img.shape)
# print (img.dtype)
# print (img.min())
# print (img.max())
# #创建窗口并显示图像
# cv2.namedWindow("Image")
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# #释放窗口
# cv2.destroyAllWindows()
