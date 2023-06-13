def hello_name():
    message=input("What is your name?: ")

    print(message)
print(hello_name())

def first_odds():
    x=1
    while True:
        print(x)
        x+=2
        if x>100:
            break
print(first_odds())

def max_num_in_list(a_list):
    
    return max(a_list)

max_num_in_list([1,2,5,3])

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





def is_consecutive(a_list):
    my_list=sorted(a_list)
    if my_list == list(range(min(a_list),max(a_list)+1)):
        print("Consecutive")
    else:
        print("Not Consecutive")

is_consecutive([1,2,4,5])

