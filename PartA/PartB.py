# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr"
message1 = "Wkh frxqw zdv ehwwhu lq wkh sodfh zlwk d udqgrpob grqdog exw lw lqwhqghg wr eh vwloo\
xvhixoob iru hyhu wkh lqwhuidfhv lq wkhlu wudfnv"

# frequency of each letter
letter_counts = Counter(message)


# find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items():
    print(letter, ":", freq)
    # INSERT CODE TO REMEMBER MAX

    # this sets the frequency of each letter that progressievly has a higher frequency than the largest one prior.
    # Of course the letter that appears first will be set as the max frequency initially because the maxFreq was
    # first set to -1. This also removes the " " space string from being considered, as with most longer sentences,
    # it will be the most prevalent.

    if freq > maxFreq and letter != " ":
        maxFreq = freq
        maxLetter = letter

print("Max Ocurring Letter:", maxLetter)

# predict shift
# assume max letter is 'e'
letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# since the letter e is the max number, creating a shift
# from where it is numerically in the alphabet is done here.
for index, letter in enumerate(letters):
    if letter == maxLetter:
        shift = index - 4



##shift = #COMPUTE SHIFT HERE
print("Predicted Shift:", shift)

offset = shift
totalLetters = 26
keys = {}
invkeys = {}

# for ease of readability, shift was renamed as offset here,
# and the index position was accordingly shifted under
# the modular of total letters to account for capital letters
for index, letter in enumerate(letters):

    # lower case letter
    if index < totalLetters:
        keys[letter] = letters[(index + offset) % totalLetters]

    # upper case letter
    else:
        keys[letter] = letters[(index + offset) % totalLetters].upper()

invkeys = dict(map(reversed, keys.items()))

# decrypting message
encryptedMessage = message
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ':  # spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage))
