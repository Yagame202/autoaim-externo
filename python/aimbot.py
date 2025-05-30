import cv2
import numpy as np
import serial
import time
import mss

arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

REGION_WIDTH = 400
REGION_HEIGHT = 400

with mss.mss() as sct:
    monitor = sct.monitors[1]
    screen_width = monitor["width"]
    screen_height = monitor["height"]

    region = {
        "left": int(screen_width / 2 - REGION_WIDTH / 2),
        "top": int(screen_height / 2 - REGION_HEIGHT / 2),
        "width": REGION_WIDTH,
        "height": REGION_HEIGHT
    }

    while True:
        img = np.array(sct.grab(region))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest)

            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                target_x = REGION_WIDTH // 2
                target_y = REGION_HEIGHT // 2

                dx = cx - target_x
                dy = cy - target_y

                move_x = int(dx * 0.4)
                move_y = int(dy * 0.4)

                if abs(move_x) > 1 or abs(move_y) > 1:
                    command = f"{move_x},{move_y}\n"
                    arduino.write(command.encode())
