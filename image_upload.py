import csv
import requests

image_url = 'http://182.211.172.137:8000/photo/get'
url = "http://182.211.172.137:8000/garbage/upload"

f = open("Result.csv", 'r')
datas = csv.reader(f)

i = 0

for data in datas:
    if data[0] == "":
        continue

    with open(f"Directory_final/{data[3]}", 'rb') as file:
        response = requests.post(image_url, files={'file': (file.name, file)})

    image_uuid = response.json()['filename']

    datas = {
        'lat': f'{data[1]}',
        'lng': f'{data[2]}',
        'datetime': data[4],
        'object': 'Garbage',
        'conf': data[5],
        'image': image_uuid,
        'com': 'N'
    }

    responses = requests.post(url, json=datas)
    print(f">>{response}")
    print(f">>{responses}")
