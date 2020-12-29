import requests

# https://www.dataquest.io/blog/python-api-tutorial/
# https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request

while True:
    print("Press 1 to view all data \nPress 2 to add data \nPress 3 to delete data \nPress 4 to get specific data \nPress x to exit the program")
    mode = input("Please select an operation: ")
    if mode == "1":
        payload = {'key1':"value1",'key2':'value2'}
        response = requests.get("http://127.0.0.1:5000/status", payload)
        print(response.text)
    elif mode == "2":
        response = requests.get("http://127.0.0.1:5000/add")
    elif mode == "3":
        response = requests.get("http://127.0.0.1:5000/delete")
    elif mode == "4":
        response = requests.get("http://127.0.0.1:5000/find")
    elif mode == "x":
        break
    else:
        print("Mode selected is invalid, please try again")
