def is_leap_year(a_year):
    

        a_year = int(input("Is this year a Leap Year?: "))
        x=a_year

        if ((x % 4==0) and (x % 100!=0)) is True: 
         print("\nThe year is a leap year!")
    
        elif (x % 400==0) is True:
         print("\nThe year is a leap year!")
        else:
            print("\nThis is NOT a leap year") 

is_leap_year(0)