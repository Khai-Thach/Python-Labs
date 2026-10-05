def pyramid(size):
    valid_input = False
    while not valid_input:
        answer = int(input(size))
        if 1 <= answer <= 8:
            valid_input = True
    return answer

size = pyramid('pick a number 1 to 8: ')
if 1 <= size <= 8:
    for a in range(0,size):
        print(" "*(size-a-1)+'#'*(a+1)+" "*2+"#"*(a+1)+" "*(size-a-1))

input('press any key to exit: ')
    

