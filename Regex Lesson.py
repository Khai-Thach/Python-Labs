'''
Final Exam Prep & Hints:
pick x out of y questions to answer (e.g. 3 out of 5 to answer) 

Lists

File Reading

Monte Carlo

Turtles

Regex[regular expressions] 
#given a file, removing something from the file
#like email address, phone number, made-up emails
#pattern replacement in strings

Mystery Question [something not taught in class but can quickly learn]

*All questions weighted the same*

'''

#Florida Man
'''unique people, why?

lots of informational freedom that makes it seem that way, why important?

jeb bush accidentally revealed all Floridian's personal information that
were in the emails he dumped

Now we gonna practice making it so personal information would not be 
revealed when dumped USING REGEX'''
#probably gonna have to watch lecture and practice in regexr, not here

import re

#words that contian cat OR ( | ) dog [cat|dog]
data = open('words.txt','r')
text = data.read()

#pattern = '\w*cat\w*|\w*dog\w*'
pattern = 'cat|dog'

answer = re.findall(pattern, text)
#print(answer)
print(len(answer))

