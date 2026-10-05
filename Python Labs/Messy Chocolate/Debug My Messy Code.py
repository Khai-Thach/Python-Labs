                            #Debug My Messy Code
def main():

    print("'It’s time to go on a scavenger hunt!’")
    print("You'd be amazed how many things can go wrong!")
    print("Please enter how long you want to travel for:")

    initialPos = 7.0;
    time = float(input());
    velocity = 5.0;
    acceleration = 1.0;

# there is a math error in here causing
# an incorrect answer in the line below

    position = initialPos + velocity * time + (1 / 2) *acceleration*time*time;

#if you are stuck on the math error, look at the footnote

    print("Length of travel: ", position);
main ()

input("Press any key to close.")
#There is a math error you must fix in the code. The program will still run, but you
#you need to fix it to get full credit. The math error stems from the 1/2
#in the code. Think what happens when you do integer division in Python.
