                           #Chocolate is All I Need

Weight = input("weight in pounds: ")
Weight = float(Weight)

Height = input("height in inches: ")
Height = float(Height)

Age = input("age in years: ")
Age = float(Age)

Male_BMR = float(655.1+(6.2*(Weight))+(12.7*(Height))-(6.76*(Age)))
print("Your male BMR is:", Male_BMR)
print("This is how many chocolate bars you can eat: ")

choco = 214
num_of_choco = int(Male_BMR/choco)
print(num_of_choco)

Female_BMR = float(655.1+(4.35*(Weight))+(4.7*(Height))-(4.7*(Age)))
print("Your Female BMR is:", Female_BMR)
print("And this is how many chocolate bars you can eat: ")

choco = 214
num_of_choco = int(Female_BMR/choco)
print(num_of_choco)

input("Press any key to leave this screen")
