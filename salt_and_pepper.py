import cv2
import numpy as np

def filter2D(img, filter):
    R,C = img.shape
    result = np.zeros((R,C), dtype=np.uint8)
    filter_R, filter_C = filter.shape
    pad_r = filter_R//2
    pad_c = filter_C//2
    for r in range(pad_r, R-pad_r):
        for c in range(pad_c , C-pad_c):
            grid = img[r-pad_r:r+pad_r+1, c-pad_c:c+pad_c+1]
            result[r,c] = max(0, np.sum(grid * filter))
    return result

size = int(input("kernel size? "))
blur_filter = np.ones((size,size)) / size**2

image1 = cv2.imread('resources/xray_noisy.png', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('resources/image_noisy.png', cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread('resources/board_noisy.png', cv2.IMREAD_GRAYSCALE)
blur1 = filter2D(image1, blur_filter)
blur2 = filter2D(image2, blur_filter)
blur3 = filter2D(image3, blur_filter)

cv2.imwrite(f"outputs/xray_blur_{str(size)}.png", blur1)
cv2.imwrite(f"outputs/image_blur_{str(size)}.png", blur2)
cv2.imwrite(f"outputs/board_blur_{str(size)}.png", blur3)
