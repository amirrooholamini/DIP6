import cv2
import numpy as np

def filtering(img, filter):
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

filter = np.array([[-1,-1,-1],
          [-1,8,-1],  
          [-1,-1,-1]])

lion = cv2.imread("resources/lion.png", cv2.IMREAD_GRAYSCALE)
spider = cv2.imread("resources/spider.webp", cv2.IMREAD_GRAYSCALE)
print("lion edges ...")
lion_edges = filtering(lion, filter)
print("completed")
print("lion edges ...")
spider_edges = filtering(spider, filter)
print("completed")

cv2.imwrite("outputs/lion_edges.png", lion_edges)
cv2.imwrite("outputs/spider_edges.png", spider_edges)
