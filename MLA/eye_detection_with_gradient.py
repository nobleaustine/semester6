import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

image = plt.imread("C:\\NOBLEAUSTINE\\documents\\me\\photo3.jpg")
image = np.mean(image, axis=-1)
image = image[2:]
sobel_filter_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_filter_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

gradient_x = ndimage.convolve(image, sobel_filter_x)
gradient_y = ndimage.convolve(image, sobel_filter_y)

gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
max_gradient_indices = np.argwhere(gradient_magnitude == np.max(gradient_magnitude))


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gradient Magnitude')
plt.imshow(gradient_magnitude, cmap='viridis')

plt.scatter(max_gradient_indices[:, 1], max_gradient_indices[:, 0], s=10, c='red', marker='o')
plt.axis('off')

plt.show()
