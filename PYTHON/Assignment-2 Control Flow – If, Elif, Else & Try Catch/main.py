print ("\nPlease enter your age: ", end="")
x = input ()
try:
    x = int(x)
    if x < 0:
        print ("Invalid input: Age cannot be negative.")
    elif x < 13:
        print ("You are categorized as: Child")
    elif x < 20:
        print ("You are categorized as: Teenager")
    elif x < 60:
        print ("You are categorized as: Adult")
    else:
        print ("You are categorized as: Senior")
except ValueError:
    print ("Invalid input: Age cannot be a non-number.")