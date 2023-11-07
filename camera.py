import cv2
import time
import os
import shutil
from datetime import datetime

ques = int(input())
output_directory = "./Direct"

shutil.rmtree(output_directory)
os.mkdir(output_directory)

webcam = cv2.VideoCapture(0)

start_time = time.time()

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        folder_path = './Direct'
        now = datetime.now()
        now0 = now.strftime('%Y-%m-%d_%H-%M-%S')
        cv2.imshow("test", frame)
        cv2.imwrite(f"{folder_path}/{now0}.jpg", frame)
        print(">>Store Complete")

    if time.time() - start_time > ques:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(2)
webcam.release()
cv2.destroyAllWindows()



