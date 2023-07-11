# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import time

import enigma
import rotor

# this is provided as the skeleton of the given code,
# but was not used in this implementation,
# rather just a list of capitals were used.
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]


ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"

# Known message at the end of the encrypted message.
crib = "Hail Shakes!"
crib_substring = ""


##Break the code via brute force search
#INSERT CODE HERE

# has the crib "Hail Shakes!"
# fixed but unknown windows/key
# still no plugboard

# A boolean for if a match for the crib has been found
match = False

# List of capital letters to generate the series of keys to
# brute force search.
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# These are used to represent each rotor, with the first
# rotor being interacted with last, and the initial
# input of a letter travels through the third window,
# then the second, then the first.

first_window_number = 0
second_window_number = 0
third_window_number = 0

# A boolean for if the message has been decoded
message_decoded = False

# Counter used to display the number of iterations used
# to decrypt Shakes' message.
counter = 0


while match == False:
    # this just sets up the rotors to move when the number of the previous
    # rotor has reached its max value
    word = ""
    message_list = []
    if third_window_number == 25:
        third_window_number = 0
        second_window_number = second_window_number + 1
    elif second_window_number == 25:
        first_window_number = first_window_number + 1
        second_window_number = 0
        third_window_number = 0

    # The keys used in the enigma machine are generated
    window3 = capital_letters[third_window_number]
    window2 = capital_letters[second_window_number]
    window1 = capital_letters[first_window_number]

    keys_to_use = window1 + window2 + window3

    engine_partC = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                 rotor.ROTOR_II, rotor.ROTOR_III, key=keys_to_use,
                                 plugs="AA BB CC DD EE")

    secret = engine_partC.encipher(ShakesHorribleMessage)

    # This splits the attempt at decrypting message by words,
    # this is used to compare to the crib, with the potentially correct
    # decryption of the crib being the last two elements of the list
    split_secret = secret.split(" ")

    unified_word = " ".join([split_secret[-2], split_secret[-1]])

    # To indicate an attempt was made at decrypting in this
    # iteration.
    counter = counter + 1

    # The booleans are made true if crib match found
    # match being True stops the iteration
    # message_decoded being True prints the details of decryption.
    if unified_word == crib:
        message_decoded = True
        match = True

    third_window_number = third_window_number + 1

#Print the Decoded message
#INSERT CODE HERE

if message_decoded == True:
    print("Number of attempts to brute force search", counter)
    print("Time taken to compute:", time.process_time(), "seconds")
    print(secret)

