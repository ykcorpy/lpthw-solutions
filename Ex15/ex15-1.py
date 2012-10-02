# imports argv from the sys module
from sys import argv

# unpacks whatever is in argv and assigns it to the variables on the left, in order
script, filename = argv

# assigns a file object to the variable txt
txt = open(filename)

# prints a string
print "Here's your file %r:" % filename

# prints the output of a function call on the txt variable
print txt.read()

# prints a string
print "Type the filename again:"

# displays the character ">", takes an input, converts it to a string and assigns it to the file_again variable
file_again = raw_input("> ")

#  assigns a file object to the txt_again variable
txt_again = open(file_again)

# prints the output of a function call on the txt_again variable
print txt_again.read()
