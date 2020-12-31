from time import sleep

import requests

import os
import webbrowser


while True:
    response = requests.get("https://13.210.116.73:5000/")
    path = os.path.abspath('temp.html')
    url = 'file://' + path
    with open(path, 'w') as f:
        f.write(response.text)
    webbrowser.open(url, new=2)

    sleep(5)





