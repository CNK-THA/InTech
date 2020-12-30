from time import sleep

import requests

import os
import webbrowser


while True:
    response = requests.get("http://127.0.0.1:5000/")
    path = os.path.abspath('temp.html')
    url = 'file://' + path
    with open(path, 'w') as f:
        f.write(response.text)
    webbrowser.open(url, new=2)

    sleep(5)





