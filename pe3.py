#
# FUNCTIONS: A
#

import string
alphabet = list(string.ascii_lowercase)

def encode(input_text,shift):
    shifted_text = ''

    for letter in list(input_text):

        if letter in alphabet:

            letter_index = alphabet.index(letter)
            shift_index = letter_index + shift
            
            if shift_index < len(alphabet):
                new_letter = alphabet[shift_index]
            else:
                new_index = (letter_index + shift) % len(alphabet)
                new_letter = alphabet[new_index]

            shifted_text += new_letter
       
        else:
            shifted_text = shifted_text + letter

    print((alphabet,shifted_text))
    return (alphabet,shifted_text)

#encode ("a", 3) # should return ([" a" , "b" , ... "z"] , "d")
#encode (" abc", 4 ) # should return ([" a" , "b" , ... "z"] , " efg ")
#encode (" xyz", 3 ) # should return ([" a" , "b" , ... "z"] , " abc ")
#encode ("j!K,2?", 3) # should return ([" a" , "b" , ... "z"] , "m!n,2 ?")

#
# FUNCTIONS: B
#

def decode(input_text,shift):
    shifted_text = ''

    for letter in list(input_text):

        if letter in alphabet:

            letter_index = alphabet.index(letter)
            shift_index = letter_index - shift
            
            if shift_index < len(alphabet) and shift_index > 0:
                new_letter = alphabet[shift_index]
            else:
                new_index = (letter_index - shift) % len(alphabet)
                new_letter = alphabet[new_index]

            shifted_text += new_letter
       
        else:
            shifted_text = shifted_text + letter
    
    print((alphabet,shifted_text))
    return (alphabet,shifted_text)

#decode ("d", 3) # should return "a"
#decode (" efg", 4 ) # should return " abc "
#decode (" abc", 3 ) # should return " xyz "
#decode ("m!n,2?", 3) # should return "j!K,2 ?"

#
# CLASSES: A
#

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
        if self.amount < 0:
            raise Exception("You may not deposit negative amounts.")
        else:
            self.balance = self.balance + self.amount
            f"Your updated account balance is ${self.balance}."
            return self.balance
    
    def withdraw(self,amount):
        new_balance = self.balance - self.amount
        if new_balance < 0:
            raise Exception("Your account will be overdrafted if you withdraw this amount.")
        else:
            self.balance = new_balance 
            f"Your updated account balance is ${self.balance}."
            return self.balance



