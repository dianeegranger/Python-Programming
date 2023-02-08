"""
Diane E. Granger
dianeegranger@gmail.com

Filename:  fortuneCookie.py

Create a program that generates random fortune cookie messages.
The program should display one of three messages each time it is run:
"Today will be a lucky day", "You will meet someone new and interesting",
or "Watch out for obstacles in your path".
To do this, you can use the random module and the if and elif statements
to select one of the messages at random.
"""

import random

lucky_number = random.randint(1, 100)     # Return random integer in range [0, 100], including both end points

fortune_cookie = random.randint(1, 3)     # Return random integer in range [1, 3], including both end points

fortune_message = ''

if fortune_cookie == 1:
    fortune_message = "Today will be a lucky day"
elif fortune_cookie == 2:
    fortune_message = "You will meet someoone new and interesting"
elif fortune_cookie == 3:
    fortune_message = "Watch out for obstacles in your path"

print(f"{fortune_message} and your lucky number is {lucky_number}")


# TERMINAL OUTPUT:

# PS C:\Users\diane\Python> python -u "c:\Users\diane\ython\fortuneCookie.py"
# Today will be a lucky day and your lucky number is 60

# PS C:\Users\diane\Python> python -u "c:\Users\diane\Python\fortuneCookie.py"
# Watch out for obstacles in your path and your lucky number is 54

# PS C:\Users\diane\Python>python -u "c:\Users\diane\Python\fortuneCookie.py"
# Today will be a lucky day and your lucky number is 33

# PS C:\Users\diane\Python>python -u "c:\Users\diane\Python\fortuneCookie.py"
# Today will be a lucky day and your lucky number is 57

# PS C:\Users\diane\Python>python -u "c:\Users\diane\Python\fortuneCookie.py"
# Watch out for obstacles in your path and your lucky number is 53

# PS C:\Users\diane\Python> python -u "c:\Users\diane\Python\fortuneCookie.py"
# Watch out for obstacles in your path and your lucky number is 87

# PS C:\Users\diane\Python> python -u "c:\Users\diane\Python\fortuneCookie.py"
# Watch out for obstacles in your path and your lucky number is 45

# PS C:\Users\diane\Python> python -u "c:\Users\diane\Python\fortuneCookie.py"
# You will meet someoone new and interesting and your lucky number is 61

# PS C:\Users\diane\Python> python -u "c:\Users\diane\Python\fortuneCookie.py"
# Today will be a lucky day and your lucky number is 67

# PS C:\Users\diane\Python> python -u "c:\Users\diane\Python\fortuneCookie.py"
# You will meet someoone new and interesting and your lucky number is 30

# PS C:\Users\diane\Python> 
