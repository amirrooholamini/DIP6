import cv2
import numpy as np

size = 31

blur_filter = np.ones((size,size)) / size**2
pad = size // 2

threshold = 150

image = cv2.imread("resources/flower_input.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
R,C = image.shape
result = np.zeros((R,C), dtype=np.uint8)

for r in range(pad, R-pad):
    for c in range(pad , C-pad):
        if image[r,c] <= threshold:
            grid = image[r-pad:r+pad+1, c-pad:c+pad+1]
            result[r,c] = np.sum(grid * blur_filter)
        else:
            result[r,c] = image[r,c]

result = cv2.resize(result, (0,0), fx=0.6, fy=0.6)
cv2.imshow("1", result)
cv2.waitKey()