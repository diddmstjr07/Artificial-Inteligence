import csv
import requests

image_url = 'http://182.211.172.137:8000/photo'
url = "http://127.0.0.1:8000/upload/garbage"

f = open("Result.csv", 'r')
datas = csv.reader(f)

i = 0

for data in datas:
    i = i + 1
    if data[0] == "":
        continue

    with open(f"Directory_final/{data[2]}", 'rb') as file:
        response = requests.post(image_url, files={'file': (file.name, file)})

    image_uuid = response.json()['filename']

    datas = {
        'lat': f'35.1246187{i}',
        'lng': f'126.908036{i}',
        'datetime': data[3],
        'object': 'Garbage',
        'conf': data[4],
        'img': image_uuid,
    }

    responses = requests.post(url, json=datas)
    print(f">>{response}")
    print(f">>{responses}")
