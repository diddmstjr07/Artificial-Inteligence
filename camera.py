import cv2
import time
import os
import shutil

# 웹캠 열기
cap = cv2.VideoCapture(0)

output_directory = "/Users/user/Desktop/Folder/yolov5-master/Direct/"

shutil.rmtree(output_directory)
os.mkdir(output_directory)

try:
    while True:
        # 프레임 읽기
        ret, frame = cap.read()

        timestamp = int(time.time())
        file_name = f"{output_directory}capture_{timestamp}.png"

        cv2.imshow('camera', frame)
        cv2.imwrite(file_name, frame)

        time.sleep(3)

except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()