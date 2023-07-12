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

image = cv2.imread('resources/building.png', cv2.IMREAD_GRAYSCALE)

vertical_kernel = np.array([[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]])

horizontal_kernel = np.array([[-1, -1, -1],
                              [ 0,  0,  0],
                              [ 1,  1,  1]])

vertical_edges = filter2D(image, vertical_kernel)
horizontal_edges = filter2D(image, horizontal_kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Vertical Edges', vertical_edges)
cv2.imshow('Horizontal Edges', horizontal_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()