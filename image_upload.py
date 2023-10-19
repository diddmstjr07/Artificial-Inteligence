import requests
import os
from datetime import datetime
from io import StringIO

url = "http://127.0.0.1:8000/upload/garbage"
image_url = 'http://182.211.172.137:8000/photo'


filenames = os.listdir('/Users/user/Desktop/Folder/yolov5-master/Direct')
for filename in filenames:
    now = datetime.now()
    now0 = now.strftime('%Y-%m-%d %H:%M:%S')

    full_filename = os.path.join('/Users/user/Desktop/Folder/yolov5-master/Direct', filename)
    file_path = full_filename

    with open(file_path, 'rb') as file:
        response = requests.post(image_url, files={'file': (file.name, file)})

    image_filename = response.json()['filename']
    address = image_filename.split('filename')[-1]

    datas = {
        'lat': '125.129380',
        'lng': '35.1820938',
        'datetime': f'{now0}',
        'object': 'Garbage',
        'conf': '12',
        'img': address,
    }

    responses = requests.post(url, json=datas)

    print('Photo Server Upload >>', response)
    print('DataBase Upload >>', responses)

