# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "The quick brown fox jumped over the lazy dog"  # type your message here
message2 = "The quick brown fox jumps over the lazy dog the five boxing wizards jump quickly how vexingly quick daft zebras jump waltz bad nymph for quick jigs vex sphinx of black quartz judge my vow pack my box with five dozen liquor jugs the jay pig fox zebra and my wolves quack blowzy night frumps vexd Jack Q the quick onyx goblin jumps over the lazy dwarf the lazy dwarf curses and mumbles"
message3 = "The quick brown fox jumps over the lazy dog the five boxing wizards jump quickly how vexingly quick daft zebras jump waltz bad nymph for quick jigs vex sphinx of black quartz judge my vow pack my box with five dozen liquor jugs the jay pig fox zebra and my wolves quack blowzy night frumps vexd Jack Q the quick onyx goblin jumps over the lazy dwarf the lazy dwarf curses and mumbles the quick brown fox jumps over the lazy dog the five boxing wizards jump quickly how vexingly quick daft zebras jump waltz bad nymph for quick jigs vex sphinx of black quartz judge my vow pack my box with five dozen liquor jugs the jay pig fox zebra and my wolves quack"

print("Message:", message)

# create the Caesar cypher
offset = 5  # choose your shift
totalLetters = 26
keys = {}  # use dictionary for letter mapping
invkeys = {}  # use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters:  # lowercase
        # INSERT CODE HERE


        # I'm assigning each letter from letters to its corresponding index position with a shift
        # from the assigned offset, of which is divided modulo by the number of letters in the
        # alphabet. The modulo is to prevent a non-capital letter being encrypted/decrypted to
        # a capital, and vice versa for when the code is decrypted.
        keys[letter] = letters[(index + offset) % totalLetters]

    else:  # uppercase
        # INSERT CODE HERE

        # I'm assigning each letter from letters, same as for non-capital letters, but I set
        # the new corresponding letter to an uppercase to preserve the case-instance.
        keys[letter] = letters[(index + offset) % totalLetters].upper()
print("Cypher Dict:", keys)

# the reversed key word returns a mapping of the key-value pairs from items
# dict() creates a dictionary
# map() processes the iterable without using an explicit for loop

invkeys = dict(map(reversed, keys.items()))

# encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ':  # spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage))  # join is used to put list into string

# decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ':  # spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage))  # join is used to put list into string

