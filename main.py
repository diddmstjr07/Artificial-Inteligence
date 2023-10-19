import shutil
import torch
import cv2
from PIL import Image
import time
import os

# folder_path = '/Users/user/Desktop/Folder/yolov5-master/Direct'
# os.makedirs(folder_path)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/user/Desktop/Folder/yolov5-master/runs/train/Garbage_result/weights/best.pt')

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    time_status = time.time()
    status, frame = webcam.read()

    models = model(frame)

    if models.xyxy[0].shape[0] > 0:
        for det in models.xyxy[0]:
            class_id, conf, x_min, y_min, x_max, y_max = det.tolist()
            class_name = model.names[class_id]
            print(f"Class: {class_name}, Confidence: {conf:.2f}")

        # cv2.imwrite(f"Direct/captured_image_{int(time_status)}.jpg", frame)
        # print('store complete')

    time.sleep(1)

    if status:
        cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        folder_path = '/Users/user/Desktop/Folder/yolov5-master/Direct'
        shutil.rmtree(folder_path)
        break

webcam.release()
cv2.destroyAllWindows()
