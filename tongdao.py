from PIL import Image

img = Image.open('C:\\Users\\lc\\Desktop\\TIF\\Python\\carShadow_infrared.jpg')
# 直接就输出图像的通道数了
print(len(img.split()))