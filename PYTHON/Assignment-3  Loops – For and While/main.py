# Array of foods
food = ["Pizza", "Burger", "Chicken", "Rice", "Fries"]
# For loop to print each food
for y in food:
    print(y)
# While loop to countdown from a positive number
print("\n")
try:
    user = int(input("Enter a positive number to start the countdown: "))
    # Check if the input is a positive number
    if user < 0:
        print ("Invalid input: Please enter a positive number")
    else:
        # Countdown
        while user > 0:
            print (user)
            user -= 1
            if user == 0:
                print ("Countdown complete!")
except:
    # If the input is not a number
    print ("Invalid input: Please enter a positive number")
