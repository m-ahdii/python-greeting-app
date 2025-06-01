# This program greets the user and asks for feedback
name = input("Enter your name: ")
day = input("Enter the current day of the week: ")
print(f"Hello, {name}! Happy {day}!")

def get_feedback():
    feedback = input("What do you think about this greeting program? ")
    print("Thank you for your feedback!")
    
get_feedback()