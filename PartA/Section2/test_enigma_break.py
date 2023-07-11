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
crib = "Hail Shakes"
crib_substring = "Gdwm Qopjmw!"
print(crib_substring)

# has the crib "Hail Shakes!"
# fixed but unknown windows/key
# still no plugboard
# you could consider the different order of the rotors


##Break the code via brute force search
#INSERT CODE HERE
match = False
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

first_window_number = 0
second_window_number = 0
third_window_number = 0

counter = 0

word = ""


engine_partB = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key="SSC",
                             plugs="AA BB CC DD EE")
# order in machine; first rotor, second rotor, third rotor (xyz)

while match == False:
    message_list = []
    if third_window_number == 25:
        third_window_number = 0
        second_window_number = second_window_number + 1
    elif second_window_number == 25:
        first_window_number = first_window_number + 1
        second_window_number = 0
        third_window_number = 0
    # no need to add it for the first rotor, as it will reach the
    # at the point where the rotor values are 25, 25, 25
    window3 = capital_letters[third_window_number]
    window2 = capital_letters[second_window_number]
    window1 = capital_letters[first_window_number]

    keys_to_use = window1 + window2 + window3

    engine_partC = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                 rotor.ROTOR_II, rotor.ROTOR_III, key=keys_to_use,
                                 plugs="AA BB CC DD EE")


    secret1 = engine_partC.encipher(ShakesHorribleMessage)

    for letter in secret1:

        if letter != " ":
            word = word + letter
        else:
            message_list.append(word)
            word = ""
    print(secret1[-12:])
    possible_substring = secret1[-12:]
    if possible_substring == crib:
        engine_partC = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                     rotor.ROTOR_II, rotor.ROTOR_III, key=keys_to_use,
                                     plugs="AA BB CC DD EE")

        secret = engine_partC.encipher(ShakesHorribleMessage)
        print(secret)
        match = True
        # will have to change the reflector now.
        # create a new python file to reorganise this

    #if secret1[-12:]) == crib:





    third_window_number = third_window_number + 1



    counter = counter + 1



    print(counter)
    print(first_window_number, second_window_number, third_window_number)

    if engine_partC.encipher(crib) == crib_substring:

        match = True
        print("yay success")
        engine_partC = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                     rotor.ROTOR_II, rotor.ROTOR_III, key=keys_to_use,
                                     plugs="AA BB CC DD EE")

        secret = engine_partC.encipher(ShakesHorribleMessage)
        print(secret)


#secret = engine.encipher(message)

# if there is no result, then do a series of While statements
# with

#Print the Decoded message
#INSERT CODE HERE

    #engine_partC = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                 #rotor.ROTOR_II, rotor.ROTOR_III, key=keys_to_use,
                                 #plugs="AA BB CC DD EE")

    #secret = engine_partC.encipher(ShakesHorribleMessage)
    #print(secret)


print("success")