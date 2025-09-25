# PART A
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

encode ("a", 3) # should return ([" a" , "b" , ... "z"] , "d")
encode (" abc", 4 ) # should return ([" a" , "b" , ... "z"] , " efg ")
encode (" xyz", 3 ) # should return ([" a" , "b" , ... "z"] , " abc ")
encode ("j!K,2?", 3) # should return ([" a" , "b" , ... "z"] , "m!n,2 ?")