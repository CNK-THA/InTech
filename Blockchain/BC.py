"""
This file contains code for Blockchain Banking activities.
Last Modified: 28/4/2021
Author: Chanon K., chanon.kachorn@gmail.com
"""


#################################################### Activity 1 ######################################################################
class User():
    """ User class to represent each banking customer."""

    def __init__(self, clientName):
        """ Create a User class object.
        Parameters:
            clientName : str
                name of thhe banking customer
        """
        self.name = clientName
        self.amount_of_money = 0

    def display_information(self):
        """ Show User class data to standard out (screen)."""
        print(self.name, self.amount_of_money)

    def deposit_money(self, amount):
        """ Deposit money into this customer's account.
        Parameters:
            amount : int
                the amount of money to deposit
        """
        self.amount_of_money += amount

    def withdraw_money(self, amount):
        """ Withdraw money from this customer's account.
        Parameters:
            amount : int
                the amount of money to withdraw
        """
        self.amount_of_money -= amount

    def transfer_money(self, amount):
        """ Transfer money from this customer's account to another account.
        Note, will need to call receive_transfer_money of receiver's User object.
        Parameters:
            amount : int
                the amount of money to transfer
        """
        self.amount_of_money -= amount

    def receive_transfer_money(self, amount):
        """ Receive the transfer money sent by another customer
        Parameters:
            amount : int
                the amount of money received
        """
        self.amount_of_money += amount
        

def read_transactions():
    """ Open the transactions file and process the transactions inside."""

    file1 = open('Transactions.txt', 'r')
    Lines = file1.readlines()
    collectionOfCustomers = {}  # {name_of_customer (str): User class object}
    for line in Lines: # Go through all lines in the Transactions.txt file
        transactionSplitted = line.split()
        if len(transactionSplitted) > 7: # if this is the first line (line of names)
            for customer in transactionSplitted: # Go through only first line to get customer names
                collectionOfCustomers[customer] = User(customer)
        elif transactionSplitted[1] == "deposit": # call appropriate function for each transaction types
            collectionOfCustomers.get(transactionSplitted[0]).deposit_money(int(transactionSplitted[2]))
        elif transactionSplitted[1] == "withdraw":
            collectionOfCustomers.get(transactionSplitted[0]).withdraw_money(int(transactionSplitted[2]))
        elif transactionSplitted[1] == "transfer":
            collectionOfCustomers.get(transactionSplitted[0]).transfer_money(int(transactionSplitted[2]))
            collectionOfCustomers.get(transactionSplitted[3]).receive_transfer_money(int(transactionSplitted[2]))

    for customer in collectionOfCustomers.values(): # show the information to screen for debugging
        customer.display_information()


##read_transactions()  # Uncomment this line to run the code


#################################################### Activity 2 ######################################################################


import json

class Block:
    """ A Block class to represent each block in Blockchain """

    def __init__(self, previous_hash):
        """ Create a Block class object
        Parameters:
            previous_hash : str
                link to the hash of the previous block
        """
        self.previousBlockHash = previous_hash
        self.transactions = []
        self.myHash = None

    def hash_myself(self):
        """ Genereate a hash of this current block"""
        self.myHash = str(hash(str(self.transactions) + self.previousBlockHash))

    def add_transaction(self, transaction):
        """ Add a new transaction to the current block
        Parameters:
            transaction : str
                new transaction to be added
        """
        self.transactions.append(transaction)

    def show_block_details(self):
        """ Display the information of this block to screen"""
        print(self.previousBlockHash, self.transactions, self.myHash)
        
    def save_to_file(self):    
        """ Generate a json format information of this block
        Returns:
            json representation of block class
        """
        return json.dumps(self.__dict__, sort_keys=True, indent=4)


def read_transactions2():
    """ Open and read the transactions file, process the transactions storing it in blockchain"""

    file1 = open("Transactions.txt", "r")
    Lines = file1.readlines()
    counter = 0 # counting which line are we reading
    currentBlock = Block(None) # point to the current block (latest block) in our block chain
    for line in Lines: # read 1 line at a time
        if counter == 0: # this is the first line, only run once for genesis block
            genesisBlock = Block('0')
            genesisBlock.add_transaction(line)
            genesisBlock.hash_myself()
            currentBlock.previousBlockHash = genesisBlock.myHash # current block points to the genesis block
            with open("BCoutput.json", "a") as f: # saving genesis block to file
                f.write(genesisBlock.save_to_file())

        elif counter > 0 and counter % 10 == 0: # >0 menas this is not a genesis block, counter % 10 ==0 means it is divisible by 10
            currentBlock.hash_myself()
            currentBlock.show_block_details()
            with open("BCoutput.json", "a") as f:
                f.write(currentBlock.save_to_file())
            newBlock = Block(currentBlock.myHash) # newBlock is pointing to old block
            currentBlock = newBlock
            currentBlock.add_transaction(line) # every 10th transaction
        else:
            currentBlock.add_transaction(line) # 1st - 9th transations
        counter += 1

    # Handle adding the last block into file, ending block in our blockchain
    currentBlock.hash_myself()
    with open("BCoutput.json", "a") as f:
        f.write(currentBlock.save_to_file())
            
read_transactions2()