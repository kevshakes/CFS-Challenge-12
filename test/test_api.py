import base64
import requests
import pprint

file_path = 'c:/Users/Hp/Desktop/CFS-Challenge-12/img/Tuei.jpg'


if __name__ == '__main__':
    url = 'https://2q003s7im7.execute-api.us-east-1.amazonaws.com/search'

    headers = {}

    data = open(file_path, 'rb').read()  # read bytes from file
    data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
    data_base64 = data_base64.decode()  # convert bytes to string

    data = {
        'image': data_base64,
    }

    response_ai = requests.post(url, headers=headers, json=data)
    response_ai = response_ai.json()
    pprint.pprint(response_ai)
