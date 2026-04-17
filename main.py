import random
print("Enter who will play\n")
print("1.User will guess\n")
print("2.Computer will guess\n")

select=int(input())


def user_guess():
    number=random.randint(1,100)
    
    while True:
        num=int(input("Enter your guess:- "))
        if(num>number):
            print ('lower')
        elif(num<number):
            print ('higher')
        else:
            print('Your guess is correct')
            break

def computer_guess():
    low =1
    high=100
    count=1
    while True:
        mid=(low+high)//2
        print(f"computer guesses {mid}")
        
        feedback=input("Enter higher/lower/correct ").lower()
        count+=1
        
        if(feedback=="higher"):
            low=mid+1
            
        elif(feedback=="lower"):
            high=mid-1
            
        else:
            print(f'computer guesses in {count} step')
            break

if select==1:
    user_guess()
elif select==2:
    computer_guess()
else:
    print("Invalid Choice")

