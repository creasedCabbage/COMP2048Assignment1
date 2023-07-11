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
import enigma
import rotor

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring = ""
print(crib_substring)

##Break the code via brute force search
#INSERT CODE HERE

# has the crib "Hail Shakes!"
# fixed but unknown windows/key
# still no plugboard
# you could consider the different order of the rotors
match = False
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

first_window_number = 0
second_window_number = 0
third_window_number = 0




while match == False:
    word = ""
    message_list = []
    if third_window_number == 25:
        third_window_number = 0
        second_window_number = second_window_number + 1
    elif second_window_number == 25:
        first_window_number = first_window_number + 1
        second_window_number = 0
        third_window_number = 0

    window3 = capital_letters[third_window_number]
    window2 = capital_letters[second_window_number]
    window1 = capital_letters[first_window_number]

    keys_to_use = window1 + window2 + window3

    engine_partC = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                 rotor.ROTOR_II, rotor.ROTOR_III, key=keys_to_use,
                                 plugs="AA BB CC DD EE")

    secret = engine_partC.encipher(ShakesHorribleMessage)

    split_secret = secret.split(" ")

    #print(message_list)

    #print(secret)

    #print(split_secret)
    print(keys_to_use)
    #print(split_secret[-2:])
    unified_word = " ".join([split_secret[-2], split_secret[-1]])

    print(unified_word)
    if unified_word == crib:
        print(secret)
        match = True

    third_window_number = third_window_number + 1

    #if split_secret[]

    #print(message_list[0])



    #print(message_list[-3])
#Print the Decoded message
#INSERT CODE HERE
