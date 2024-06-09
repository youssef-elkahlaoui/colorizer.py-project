import cv2
import numpy as np

def convert_to_grayscale(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_3_channels = np.zeros_like(frame)
    gray_3_channels[:, :, 0] = gray
    gray_3_channels[:, :, 1] = gray
    gray_3_channels[:, :, 2] = gray
    return gray_3_channels

def resize_image(image, size):
    return cv2.resize(image, size)
