import cv2
import numpy as np
import glob


folder = "images/*.tif" #path to folder
values = open('csv_files/green.csv', "w")

for imgpath in glob.glob(folder):
    image = cv2.imread(imgpath)
    # Set minimum and maximum HSV values to display
    lower = np.array([40, 40, 0])
    upper = np.array([120, 255, 255])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    # print(cv2.countNonZero(mask))
    # print(mask.size == image.size/3)
    ratio_green = cv2.countNonZero(mask) / (image.size / 3)
    text = imgpath[7:] + "," + str(np.round(ratio_green * 100, 2)) + "\n"
    values.write(text)
    # print('Green pixel percentage:', np.round(ratio_brown*100, 2))
    # print(np.count)
    # cv2.imshow("fd",result)
    # cv2.waitKey()