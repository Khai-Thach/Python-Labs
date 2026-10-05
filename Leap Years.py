# Blame Pope Gregory XIII
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    
    elif year % 400 == 0:
        return True
       
    else:    
        return False

                             #0123456789

date = input('Enter a date in MM/DD/YYYY ')


month = int(date[:2])
day   = int(date[3:5])
year  = int(date[6:])

# if the month has 30 days(September, November, June, April)

if month in [4,6,9,11]: #no need for month == x or month == x ...
    if 1 <= day <= 30:  #no need for and (day>=1 and day<=31)
        print('Valid date')
    else:
            print(day, 'is not valid')
            
    
# if the month has 31 days(August,May,October,December,January,March,july)
elif month in [8,5,10,12,1,3,7]:
    if 1<= day <=31: 
        print('Valid date')
    else:
        print(day, 'is not valid')



# if month is feb
elif month == 2:
    if 1 <= day <=28:
        print('Valid date')

    elif day > 29 and isLeapYear(year):
         print('Valid date')
         
    else:
         print(day, 'is not a valid day')
        
       
      

#else out of bounds

else:
    print(month, 'is not a valid month')
    

 
