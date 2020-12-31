import requests

# https://www.dataquest.io/blog/python-api-tutorial/
# https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request

cookie = None

print("Welcome to ABC Online Shopping")
while True:
    registered = input("Are you an existing customer? y/n: ")
    if registered == "y":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        payload = {"username": username, "password": password}
        response = requests.post("http://3.25.154.103:5000/login", payload)
        if response.text == '-2':
            print("Wrong credential, let's try that again.")
        else:
            cookie = username
            break
    elif registered == "n":
        print("Welcome, we will now sign you up to the system")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        payload = {"username": username, "password": password}
        response = requests.post("http://3.25.154.103:5000/register", payload)
        if response.text == '-1':
            print("Existing customer, please login instead.")
        else:
            cookie = username
            break
    else:
        print("Sorry I did not understand, we will try that again.")


print("Press 1 to view all items on sale \nPress 2 to buy items \nPress 3 to add credit to my account \nPress 4 to view my profile \nPress x to exit the program")

while True:
    mode = input("Please select an operation: ")
    if mode == "1":
        response = requests.get("http://3.25.154.103:5000/list")
        print(response.text)
    elif mode == "2":
        product = input("Please enter product name that you would like to purchase: ")
        payload = {"product": product, "cookie": cookie}
        response = requests.post("http://3.25.154.103:5000/buy", payload)
        print(response.text)
    elif mode == "3":
        amount = input("How much credit would you like to add: ")
        payload = {"amount": amount, "cookie": cookie}
        response = requests.post("http://3.25.154.103:5000/add_credit", payload)
        print(response.text)
    elif mode == "4":
        payload = {"cookie": cookie}
        response = requests.post("http://3.25.154.103:5000/profile", payload)
        print(response.text)
    elif mode == "x":
        break
    else:
        print("Mode selected is invalid, please try again")
