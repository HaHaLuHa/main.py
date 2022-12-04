from PIL import Image as ImagePIL, ImageFont, ImageDraw

im = ImagePIL.open('C:\\Users\\lc\\Desktop\\vis_001.jpg')
im.show("C:\\Users\\lc\\Desktop\\vis_001.jpg")
im.save('vis_001_dpi_300.jpg', dpi=(300, 300))

