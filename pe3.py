#
# FUNCTIONS
#

import string
lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

def encode(input_text,shift):
    shifted_text = ''

    for letter in list(input_text):

        alphabet = lower_alphabet
        
        letter_index = alphabet.index(letter)
        shift_index = (letter_index + shift) % len(alphabet)
        new_letter = alphabet[shift_index]
        shifted_text += new_letter

    #print((lower_alphabet,shifted_text))
    return (lower_alphabet,shifted_text)

#encode ("a", 3) # should return ([" a" , "b" , ... "z"] , "d")
#encode (" abc", 4 ) # should return ([" a" , "b" , ... "z"] , " efg ")
#encode (" xyz", 3 ) # should return ([" a" , "b" , ... "z"] , " abc ")
#encode ("j!K,2?", 3) # should return ([" a" , "b" , ... "z"] , "m!n,2 ?")

def decode(input_text,shift):
    shifted_text = ''

    for letter in list(input_text):

        if letter in lower_alphabet:
            alphabet = lower_alphabet
        elif letter in upper_alphabet:
            alphabet = upper_alphabet
        else:
            shifted_text += letter
            continue

        letter_index = alphabet.index(letter)
        shift_index = (letter_index - shift) % len(alphabet)
        new_letter = alphabet[shift_index]
        shifted_text += new_letter

    #print((lower_alphabet,shifted_text))
    return shifted_text

#decode ("d", 3) # should return "a"
#decode (" efg", 4 ) # should return " abc "
#decode (" abc", 3 ) # should return " xyz "
#decode ("m!N,2?", 3) # should return "j!K,2 ?"

#
# CLASSES
#

import datetime

class BankAccount():
    def __init__(self, name="Rainy",ID="1234",creation_date=datetime.date.today(),balance=0):
        self.name = name
        self.ID = ID
        self.balance = balance
        if creation_date > datetime.date.today():
            raise Exception("The account creation date cannot be in the future.")
        else:
            self.creation_date = creation_date
    
    def deposit(self,amount):
        if amount < 0:
            raise Exception("You may not deposit negative amounts.")
        else:
            self.balance = self.balance + amount
            f"Your updated account balance is ${self.balance}."
        return self.balance
    
    def withdraw(self,amount):
        self.balance = self.balance - amount
        f"Your updated account balance is ${self.balance}."
        return self.balance
    
    def view_balance(self):
        f"Your account balance is ${self.balance}."
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()

    def withdraw(self,amount):
        new_balance = self.balance - amount

        if new_balance < 0:
            raise Exception("Your account will be overdrafted if you withdraw this amount.")
        elif self.creation_date < date(datetime.date.today()-180):
            raise Exception("Your account must be in existence for 180 days before making any withdrawals.")
        else:
            self.balance = new_balance 
            f"Your updated account balance is ${self.balance}."
    
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__()

    def withdraw(self,amount):
        new_balance = self.balance - amount

        if new_balance < 0:
            self.balance = new_balance - 30
            f"Your account is overdrafted. You have been charged an additional $30 fee."
        else:
            self.balance = new_balance 
        
        f"Your updated account balance is ${self.balance}."
        return self.balance