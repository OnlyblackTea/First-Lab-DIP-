"""
  filename      : functions
  author        : quanzhou.li
  date          : 2024/10/20
  Description   :
"""
import math
import numpy as np

def clip_and_convert(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return np.clip(ret, 0, 255).astype(np.uint8)
    return wrapper

class BaseFunction():
    def __init__(self):
        pass

# log变换
@clip_and_convert
def T_log(r, base=2):
    norm_r = r/255 + 1
    return math.log(r, base) * 255

# 灰度反转
@clip_and_convert
def T_reverse(r):
    return 255 - r

# 线性变换
@clip_and_convert
def T_linear(r, a, b, c, d):
    """
    线性变换
    :param r: 输入像素值
    :param a: 暗处拐点输入值
    :param b: 亮处拐点输入值
    :param c: 暗处拐点输出值
    :param d: 亮处拐点输出值
    :return s: 变换后的像素值
    """
    return ((d - c) / (b - a)) * (r - a) + c