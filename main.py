import cv2
import numpy as np

foto = cv2.imread("lion.jpg",0)
cv2.imshow("aslan",foto)
cv2.waitKey()

import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread("lion.jpg")
vals = img.mean(axis=2).flatten()
counts, bins = np.histogram(vals, range(257))
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()