# Extended Caesar script

from collections import Counter
import string

message1 = "testing"
message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr"
message2 = "Khoor krz duh brx"
message3 = "Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn"
message4 = "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl ymj knaj gtcnsl bnefwix ozru vznhpqd mtb ajcnslqd vznhp ifky ejgwfx ozru bfqye gfi sdrum ktw vznhp onlx ajc xumnsc tk gqfhp vzfwye ozilj rd atb ufhp rd gtc bnym knaj itejs qnvztw ozlx ymj ofd unl ktc ejgwf fsi rd btqajx vzfhp gqtbed snlmy kwzrux ajci Ofhp V ymj vznhp tsdc ltgqns ozrux tajw ymj qfed ibfwk ymj qfed ibfwk hzwxjx fsi rzrgqjx"
message0 = "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl ymj knaj gtcnsl bnefwix ozru vznhpqd mtb ajcnslqd vznhp ifky ejgwfx ozru bfqye gfi sdrum ktw vznhp onlx ajc xumnsc tk gqfhp vzfwye ozilj rd atb ufhp rd gtc bnym knaj itejs qnvztw ozlx ymj ofd unl ktc ejgwf fsi rd btqajx vzfhp gqtbed snlmy kwzrux ajci Ofhp V ymj vznhp tsdc ltgqns ozrux tajw ymj qfed ibfwk ymj qfed ibfwk hzwxjx fsi rzrgqjx ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl ymj knaj gtcnsl bnefwix ozru vznhpqd mtb ajcnslqd vznhp ifky ejgwfx ozru bfqye gfi sdrum ktw vznhp onlx ajc xumnsc tk gqfhp vzfwye ozilj rd atb ufhp rd gtc bnym knaj itejs qnvztw ozlx ymj ofd unl ktc ejgwf fsi rd btqajx vzfhp"
message5 = "sqqsntwrshlpshcuhyrnrfcrhorvrk"

message = "Aoghsf vog uwjsb Rcppm o gcqy Rcppm wg tfss"

# frequency of each letter
letter_counts = Counter(message)

# find max letter
maxFreq = -1
maxLetter = None

# this is returning the frequency of letters present
# and accounting for spaces as strings
for letter, freq in letter_counts.items():
    print(letter, ":", freq)

    if freq > maxFreq and letter != " ":
        maxFreq = freq
        maxLetter = letter

print("Max Ocurring Letter:", maxLetter)

letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# the 300 most common words in english make up 65% of speech,
# so by comparing shift options to these words and measuring
# the number of matches via a decrpytion score enables the
# determination of the correct shift
most_common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with',
                     'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her',
                     'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up',
                     'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time',
                     'no', 'just', 'him', 'know', 'take', 'person', 'into', 'year', 'your', 'good', 'some', 'could',
                     'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think',
                     'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new',
                     'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', 'is', 'am', 'are', 'was', 'were',
                     'has', 'been', 'had', 'may', 'might', 'shall', 'should', 'will', 'would', 'can', 'could', 'do',
                     'does', 'did', 'must', 'ought', 'need', 'used', 'make', 'made', 'let', 'lets', 'say', 'says', 'go',
                     'goes', 'went', 'gone', 'take', 'takes', 'took', 'taken', 'come', 'comes', 'came', 'coming']

counter = 1
offset = counter
totalLetters = 26
keys = {}
invkeys = {}


word = ""


maxDecryptionScore = 0

finalShift = 0

print(""
      "These are the different decryption options of the encrypted message.")

while counter < 26:
    print("")
    words = []
    decryptionScore = 0
    print("Shift:", counter)

    for index, letter in enumerate(letters):

        if index < totalLetters:
            keys[letter] = letters[(index + counter) % totalLetters]

        else:
            keys[letter] = letters[(index + counter) % totalLetters].upper()


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

    # forming list of letters into list of words,
    # so they can be compared to most popular words in english
    for letter in decryptedMessage:

        if letter != " ":
            word = word + letter
        else:
            words.append(word)
            word = ""

    # comparing this shifted list of words to most common english words
    # then increasing the decryption score by one if so
    for word1 in words:
        for word2 in most_common_words:
            if word1.lower() == word2:
                decryptionScore = decryptionScore + 1

    print("Decryption Score:", decryptionScore)

    # the counter measures the number of iterations
    # which is the same as the number of attempted shifts
    # so when the decrpytion score is highest,
    # the counter at that time matches the correct shift.
    if decryptionScore > maxDecryptionScore:
        maxDecryptionScore = decryptionScore
        finalShift = counter



    counter = counter + 1

print("")
print("The correct shift is:", finalShift)
print("This decrypts the message to:")

# now that the correct shift has been determined,
# it can now be used to generate a shift on the
# message, per code in previous parts A and B
for index, letter in enumerate(letters):

    if index < totalLetters:
        keys[letter] = letters[(index + finalShift) % totalLetters]

    else:
        keys[letter] = letters[(index + finalShift) % totalLetters].upper()

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