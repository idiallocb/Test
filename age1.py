#ans = ''
while True:
    try:
        age = int(input("Enter your age "))
    except:
        print("Please enter a number!")
    
    #print("Would you like to continue? ")
    
    print("Your age is ", age)
    str1 = "Hello"
    print(str1 * 2)
    
    ans = input("Continue? " )
    if ans == 'n':
        break


