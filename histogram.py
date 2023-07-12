import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_hist(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    histogram = np.zeros((256), dtype=np.int16)
    s = 0
    R,C = img.shape
    for r in range(R):
        for c in range(C):
            s+=1
            value = img[r,c]
            histogram[value] += 1  
    return histogram
image = cv2.imread("resources/mohsen.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
flatten_image = image.flatten()
hist = get_hist(image)

plt.figure(num='histogram bar chart')
plt.bar([i for i in range(256)], hist, color="darkorange")
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('histogram bar chart')

plt.figure("histogram hist chart")
plt.hist(flatten_image, bins=256, range=(0,256), color='purple')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('histogram hist chart')

plt.figure("histogram plot chart")
plt.plot(hist, color="navy")
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('histogram plot chart')

plt.show()


