
#Regex Dictionary

import re

#1
data = open('words.txt','r')
text = data.read()

pattern = r'cat|dog'

answer = re.findall(pattern, text)

print(len(answer))


#2
data = open('words.txt','r')
text = data.read()

pattern = r'\b\w{4}\b'

answer = re.findall(pattern,text)

print(len(answer))


#3
data = open('words.txt','r')
text = data.read()

pattern = r'\w*hun\w*'

answer = re.findall(pattern,text)

print(len(answer))



#4
data = open('words.txt','r')
text = data.read()

pattern = r'\w*ing\b'


answer = re.findall(pattern,text)

print(len(answer))


pattern2 = r'\w*ion\b'

answer2 = re.findall(pattern2,text)

print(len(answer2))


'''   there are more words that end in "ing"   '''



#5
data = open('words.txt','r')
text = data.read()

pattern = r'\b\w*q(?!u)[a-z]\w*\b'


answer = re.findall(pattern,text)

print(len(answer))


#6
data = open('words.txt','r')
text = data.read()

pattern = r"\b[^aeiouAEIOU\s\-\'\d]+\b"


answer = re.findall(pattern,text)

print(len(answer))


#7
data = open('words.txt','r')
text = data.read()

pattern = r'\b\w*[AEIOUaeiou]\w*\b'


answer = re.findall(pattern,text)

print(len(answer))


#8
data = open('words.txt','r')
text = data.read()

pattern = r"\b\w*\'?n\'t\b"


answer = re.findall(pattern,text)

print(len(answer))


#9
data = open('words.txt','r')
text = data.read()

pattern = r'\b\w*[aeiouAEIOU]{2}\w*\b'


answer = re.findall(pattern,text)

print(len(answer))


#10
data = open('words.txt','r')
text = data.read()

pattern = r'\b\w*[aeiouAEIOU]\w*[aeiouAEIOU]\w*\b'


answer = re.findall(pattern,text)

print(len(answer))


#More Regex

#1
'''
.* matches all texts it can

.*? matches as little text as it can

'''

#2
Nakamoto = "Omori Nakamoto, Satoshi Nakamoto, Alice Nakamoto, RoboCop Nakamoto, satoshi Nakamoto, Mr. Nakamoto, Nakamoto, Satoshi nakamoto"

pattern = r'\b[A-Z][a-zA-Z]*\sNakamoto\b'
answer = re.findall(pattern, Nakamoto)

print(answer)


#3
numbers = "thirty, thirty-eight, seventy-two, eighty-three, sixty-seven, ninety-nine"

pattern = r'(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)|(?:one|two|three|four|five|six|seven|eight|nine)'
answer = re.findall(pattern, numbers)

print(answer)


#4
money = "$100.00, $10,000.00, $1234, $5000.00, $1,000,000, $1000000000000, $18.95"

pattern = r'\$\d{1,}(?:,\d{3})*(?:\.\d{2})?'
answer = re.findall(pattern, money)

print(answer)


#Strong Password Detection
def strongPassword(password):

    if len(password) < 8:
        return False


    if not re.search(r'[A-Z]', password):
        return False


    if not re.search(r'[a-z]', password):
        return False


    if not re.search(r'\d', password):
        return False


    return True

print(strongPassword('IndegoL@bs18')) #This came out True
print(strongPassword('chee5encr4ckerz')) #This came out False


#Kinda a Regex Problem 

import random

def betterPassword(filename):

    text =  open(filename, 'r')
    words = []
    
    for line in text:
        words.append(line.strip())
        
    filteredWords = []
    for word in words:
        if len(word) >= 4:
            filteredWords.append(word)

    makePassword = random.sample(filteredWords, 4)

    password = ''.join(makePassword)

    return password


print(betterPassword('words.txt'))

