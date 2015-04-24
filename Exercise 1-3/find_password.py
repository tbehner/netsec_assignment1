import re
import crypt, getpass, pwd

# encrypt word with salt using c crypt
def encryptWord(word, salt):
    encrypted_word = crypt.crypt(word, salt)
    return encrypted_word

# split line into words, don't only split at blanks but also at other symbols
def splitInWords(line):
    #words = line.split()
    words = re.findall(r"[\w']+", line)
    return words

# read file and return all lines
def readFile(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return lines

# read file and return all lines
def findPassword(lines):
    for line in lines:
        words = splitInWords(line)
        # encrypt each word with the salt (first two characters of known crypt c string) and find match
        for word in words:
            encrypted_word = encryptWord(word, "Ae")
            if encrypted_word == "Aedm1ab9f4MjA":
                print word
                print encrypted_word
            #print "%s %s" % (word, encryptWord(word, "Ae"))


# read file and find the password in it
file_name = "rfc7511.txt"
lines = readFile(file_name)
findPassword(lines)
