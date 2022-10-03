# the IF keyword
name = input("enter name: ")
age = input("enter ur age:")

if name == 'franklin' and age >= str(12): # if statement is ussed as a condition statement
    print("hello franklin")
elif age < str(12):
    print('are not alice kiddo')
else:
    print("done")
# else Statements
# An if clause can optionally be followed by an else statement. The else
# clause is executed only when the if statement’s condition is False. In plain
# English, an else statement could be read as, “If this condition is true, execute
# this code. Or else, execute that code.” An else statement doesn’t have
# a condition, and in code, an else statement always consists of the following:
# • The else keyword
# • A colon
# • Starting on the next line, an indented block of code (called the
# else clause)

# # Returning to the Alice example, let’s look at some code that uses an
# # else statement to offer a different greeting if the person’s name isn’t Alice.

'''else: 
    print("hello, stranger")'''
# elif Statements
# While only one of the if or else clauses will execute, you may have a case
# where you want one of many possible clauses to execute. The elif statement
# is an “else if” statement that always follows an if or another elif statement. It
# provides another condition that is checked only if all of the previous conditions
# were False. In code, an elif statement always consists of the following:
# • The elif keyword
# • A condition (that is, an expression that evaluates to True or False)
# • A colon
# • Starting on the next line, an indented block of code (called the
# elif clause)
# Let’s add an elif to the name checker to see this statement in action.
'''if name == 'franklin': # if statement is ussed as a condition statement
    print('hi, franklin')'''
    