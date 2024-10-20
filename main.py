"""
  filename      : main
  author        : quanzhou.li
  date          : 2024/10/20
  Description   :
"""

from tools import ImageHandler

# 读取图片，查看图片、直方图、频率图信息
image_handler = ImageHandler(image_path='resources/test1_1.jpg', _convert='L')

# 绘制直方图
image_handler.draw_histogram()

# 对图像应用线性变换，压低暗部，提高亮部
image_handler.linear_transform()
image_handler.save()