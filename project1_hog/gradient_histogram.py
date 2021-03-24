import cv2
import numpy as np


def get_grad_hist(img_array, point, distance=3, bins=10):
    sobel_x = cv2.Sobel(img_array, cv2.CV_32F, 1, 0, 1)
    sobel_y = cv2.Sobel(img_array, cv2.CV_32F, 0, 1, 1)

    raw_mag, raw_ang = cv2.cartToPolar(sobel_x, sobel_y, angleInDegrees=True)

    pixel_area_size = distance * 2 + 1
    mag_array = np.zeros((pixel_area_size, pixel_area_size))
    ang_array = np.zeros((pixel_area_size, pixel_area_size))

    for i in range(pixel_area_size):
        for j in range(pixel_area_size):
            mag_array[i, j] = max(raw_mag[point[1] - 2 + i, point[0] - 2 + j])
            ang_array[i, j] = max(raw_ang[point[1] - 2 + i, point[0] - 2 + j])

    unit_angle = 360 / bins
    hist_list_raw = [0] * bins

    for i in range(pixel_area_size):
        for j in range(pixel_area_size):
            target_bin = int(ang_array[i, j] / unit_angle)
            hist_list_raw[target_bin] += mag_array[i, j]

    divisor = max(hist_list_raw)
    ret_list = []
    for i in hist_list_raw:
        ret_list.append(round((i / divisor) * 100, 3))
    return ret_list


def variance_check(lefthand: list, righthand: list):
    if len(lefthand) != len(righthand):
        raise ValueError("comparing object differs in size")
    diff_sum = 0
    for i in range(len(lefthand)):
        diff = lefthand[i] - righthand[i]
        diff_sum += diff * diff

    return diff_sum
