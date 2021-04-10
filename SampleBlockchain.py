class User:

def __init__(self, name):
self.name = name
self.amount_of_money = 0

def display_information(self):
print(self.name, "with amount of money:", self.amount_of_money)

def withdraw_money(self, amount):
self.amount_of_money -= int(amount)

def deposit_money(self, amount):
self.amount_of_money += int(amount)

def transfer_money(self amount):
self.amount_of_money -= int(amount)

def receive_transfer_money(self, amount):
self.amount_of_money += int(amount)


def read_transactions():
users = {}
file = open("Transactions.txt", "r")
firstLine = True
for transaction in file:
transaction = transaction.split()
if firstLine:
for customer in transaction:
users[customer] = User(customer)
if transaction[1] == "transfer":
#### use enum here? or stick to dict####
users.get(transaction[0]).transfer_money(transaction[2])
users.get(transaction[3]).receive_transfer_money(transaction[2])
elif transaction[1] == "deposit":
users.get(transaction[0]).deposit_money(transaction[2])
elif transaction[1] == "withdraw":
users.get(transaction[0]).withdraw_money(transaction[2])

for users in users.values():
users.display_information()


class Block
def __init__(self, previous_hash):
self.previousBlockHash = previous_hash
self.transactions = []
self.myHash = None

def hash_myself(self):
self.myHash = hash(self.previousBlockHash + self.transactions)

def add_transaction(self, transaction):
self.transactions.append(transaction)

def show_block_details(self):
print("previous block", self.previousBlockHash)
print("transactions", self.transactions)
print("my Hash", self.myHash)

