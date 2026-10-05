consonants= "pkhlmnw' "
singleVowels= {"a": "ah", "e":"eh", "i": "ee", "o": "oh", "u": "oo"}
doubleVowels= {"ai": "eye", "ae": "eye", "ao": "ow", "au":"ow", "ei":"ay",
               "eu":"eh-oo","iu":"ew","oi":"oyo","ou":"ow","ui":"ooey"}

def validate(word):
    for letter in word.lower():
        if letter not in ["p","k","h","l","m","n","w","'"," ","a","e","i","u","o"]:
            print(letter, "is not a valid hawaiian character")
            return False
    return True
    
def pronounce(word):
    word = word.lower()
    output= ""
    index = 0

    while index < len(word):
        letter = word[index]
        letterAndNext = word[index:index + 2]
        specialCase = word[index-1:index+1]
        
        if letterAndNext in doubleVowels:
            output += doubleVowels[letterAndNext] + "-"
            index += 2
            if index >= len(word):
                break
            
        elif letter in singleVowels:
            output += singleVowels[letter] + "-"
            index += 1
            
        elif letter in consonants:
            if letter == "'":
                output = output[:-1]
                
            if letter == " ":
                output = output[:-1]     
            output += letter
            
            if specialCase == "ew" or specialCase == "iw":
                output = output.replace("w", "v")      
            index += 1

    output = output[0].upper() + output[1:-1]
    
    print(word.capitalize(), "is pronounced", output)

def mainLoop():
    statement = False
    
    while True:
        hawaiian = " "

        while not statement:     
            hawaiian = input("Enter a Hawaiian word to pronounce ==> ")

            statement = validate(hawaiian)

        pronounce(hawaiian)

        statement = False

        while True:
            check = input("Do you want to enter another word? Y/YES/N/NO ==> ").upper()

            if check in ['Y', 'YES']:
                break
            
            elif check in ['N', 'NO']:
                print("Thank you for playing!")
                return
            
            else:
                print("Please enter Y/YES or N/NO")
                

mainLoop()
