def create_greeting(name):
    return f"Hello {name}!, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

name = input("Please input your name: ")
if name.isalpha():
    print ("The Greeting Message Is: ", end="")
    print (create_greeting(name))
else:
    print ("Invalid input: Please enter a valid name.")



