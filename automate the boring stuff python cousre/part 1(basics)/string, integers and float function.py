# You used the int() and str() functions in the last three lines of your
# program to get a value of the appropriate data type for the code.
from cgi import print_directory
from pickletools import int4


print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
print('i have eaten' + str(int(123)) + 'banana')