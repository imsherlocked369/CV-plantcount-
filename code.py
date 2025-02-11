import cv2
import numpy as np

def count_plants_opencv(image_path):
    # Load image 
    image = cv2.imread(image_path)
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    
    lower_bound = np.array([30, 40, 40])
    upper_bound = np.array([90, 255, 255])
    
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
   
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    plant_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]
    
    # Draw contours 
    output = image.copy()
    cv2.drawContours(output, plant_contours, -1, (0, 0, 255), 2)
    cv2.imshow("Detected Plants", output)
    cv2.waitKey(0)
    
    return len(plant_contours)

if __name__ == "__main__":
    image_path = r"C:\Users\Admin\Downloads\Count1 (1).jpg" 
    count = count_plants_opencv(image_path)
    print("Plant count:", count)
