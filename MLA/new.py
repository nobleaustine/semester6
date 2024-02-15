
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the person's photo
image_path = "C:\\NOBLEAUSTINE\\documents\\me\\photo3.jpg"  # Change this to the actual path of the person's photo
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Use the Canny edge detector to detect edges
    edges = cv2.Canny(blurred_image, 50, 150)

    # Dilate the edges to make them more prominent
    dilated_edges = cv2.dilate(edges, None, iterations=2)

    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area and aspect ratio
    min_contour_area = 100
    filtered_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > min_contour_area:
            # Calculate the aspect ratio of the contour's bounding box
            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = float(w) / h

            # Adjust the aspect_ratio_threshold based on your requirements
            aspect_ratio_threshold = 1.0
            if 0.8 < aspect_ratio < aspect_ratio_threshold:
                filtered_contours.append(cnt)

    # Draw larger red dots at the centroid of each detected contour
    for contour in filtered_contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            print(cx,cy)
            cv2.circle(image, (cx, cy), 100, (0, 0, 255), -1)
    
    # Display the result
    plt.imshow(image,cmap='gray')
    plt.title('Detected Eyes with Larger Red Dots')
    plt.axis('off')
    plt.show()

