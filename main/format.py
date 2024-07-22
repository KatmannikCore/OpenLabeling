import math
from tracking import find_sign
from sign_config import *
import cv2
from skimage.color import rgb2gray

def yolo_format(class_index, point_1, point_2, width, height):
    # YOLO wants everything normalized
    # Order: class x_center y_center x_width y_height
    x_center = float((point_1[0] + point_2[0]) / (2.0 * width))
    y_center = float((point_1[1] + point_2[1]) / (2.0 * height))
    x_width = float(abs(point_2[0] - point_1[0])) / width
    y_height = float(abs(point_2[1] - point_1[1])) / height
    items = map(str, [class_index, x_center, y_center, x_width, y_height])
    return ' '.join(items)


def calculate_size_box(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    diagonal_length = math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)

    # Высота и ширина квадрата равны стороне
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return height, width


def calculate_center_box(point_1, point_2):
    x_center = int((point_1[0] + point_2[0]) / 2.0)
    y_center = int((point_1[1] + point_2[1]) / 2.0)
    return x_center, y_center


def get_minImg(x, y, w, h, img):
    x1 = x + w
    y1 = y + h
    minImg = img[y:y1, x:x1]
    minImg = cv2.resize(minImg, dsize=(28, 28))
    minImg = rgb2gray(minImg)
    return minImg


def rnn_format(class_id, point_1, point_2, img):
    height_box, width_box = calculate_size_box(point_1, point_2)
    x, y = calculate_center_box(point_1, point_2)
    minImg = get_minImg(x, y, width_box, height_box, img)

    my_json = {
        "name_one": names_signs_for_YOLO[class_id],
        "name_two": find_sign(minImg,class_id),
        "w": width_box,
        "h": height_box,
        "x": x,
        "y": y,
        "id": 0,
        "side":0,
    }
    return my_json


def voc_format(class_name, point_1, point_2):
    # Order: class_name xmin ymin xmax ymax
    xmin, ymin = min(point_1[0], point_2[0]), min(point_1[1], point_2[1])
    xmax, ymax = max(point_1[0], point_2[0]), max(point_1[1], point_2[1])
    items = map(str, [class_name, xmin, ymin, xmax, ymax])
    return items


def yolo_to_voc(x_center, y_center, x_width, y_height, width, height):
    x_center *= float(width)
    y_center *= float(height)
    x_width *= float(width)
    y_height *= float(height)
    x_width /= 2.0
    y_height /= 2.0
    xmin = int(round(x_center - x_width))
    ymin = int(round(y_center - y_height))
    xmax = int(round(x_center + x_width))
    ymax = int(round(y_center + y_height))
    return xmin, ymin, xmax, ymax
