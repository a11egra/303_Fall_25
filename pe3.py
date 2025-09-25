#
# FUNCTIONS
#

import string
lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

def encode(input_text,shift):
    shifted_text = ''

    for letter in list(input_text.lower()):

        alphabet = lower_alphabet
        if letter in lower_alphabet:
            letter_index = alphabet.index(letter)
            shift_index = (letter_index + shift) % len(alphabet)
            new_letter = alphabet[shift_index]
            shifted_text += new_letter
        else:
            shifted_text += letter

    #print((lower_alphabet,shifted_text))
    return (lower_alphabet,shifted_text)

#encode ("a", 3) # should return ([" a" , "b" , ... "z"] , "d")
#encode (" abc", 4 ) # should return ([" a" , "b" , ... "z"] , " efg ")
#encode (" xyz", 3 ) # should return ([" a" , "b" , ... "z"] , " abc ")
#encode ("j!K,2?", 3) # should return ([" a" , "b" , ... "z"] , "m!n,2 ?")

def decode(input_text,shift):
    shifted_text = ''

    for letter in list(input_text):

        if letter.lower() in lower_alphabet:
            if letter.isupper():
                letter_index = upper_alphabet.index(letter)
                shift_index = (letter_index - shift) % len(upper_alphabet)
                new_letter = upper_alphabet[shift_index]
            elif letter.islower():
                letter_index = lower_alphabet.index(letter)
                shift_index = (letter_index - shift) % len(lower_alphabet)
                new_letter = lower_alphabet[shift_index]
        else:
            new_letter = letter
            
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
        if amount > 0:
            self.balance = self.balance + amount
        print(self.balance)
        return self.balance
    
    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self.balance
    
    def view_balance(self):
        print(self.balance)
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self,name,ID,creation_date,balance):
        super().__init__()

    def withdraw(self,amount):
        datelimit = datetime.date.today() - datetime.timedelta(days=180)
        new_balance = self.balance - amount
        if new_balance > 0 and self.creation_date > datelimit:
            self.balance = new_balance

        print(self.balance)
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self,name,ID,creation_date,balance):
        super().__init__()

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance < 0:
            self.balance = new_balance - 30

        print(self.balance)
        return self.balance