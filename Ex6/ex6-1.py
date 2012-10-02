# Creates the variable x and assigns a string to it. The %d format character in the string is replaced by the integer 10.
x = "There are %d types of people." % 10

# Creates the variable binary and assigns a string to it.
binary = "binary"

# Creates the variable do_not and assigns a string to it.
do_not = "don't"

# Creates the variable y and assigns a string to it. The two %s format characters in the string are replaced  by the values stored in the variables binary and do_not.
y = "Those who know %s and those who %s." % (binary, do_not)


# Prints the string stored in the variable x.
print x

# Prints the string stored in the variable y.
print y


# Prints a string.
print "I said: %r." % x

# Prints a string.
print "I also said: '%s'." % y


# Creates the variable hilarious and assigns a Boolean value to it.
hilarious = False


# Creates the variable joke_evaluation and assigns a string to it.
joke_evaluation = "Isn't that joke so funny?! %r"


# Prints the string stored in joke_evaluation, replacing the %r format character in that string with the Boolean value stored in the variable hilarious.
print joke_evaluation % hilarious

# Creates the variable w and assigns a string to it.
w = "This is the left side of..."

# Creates the variable e and assigns a string to it.
e = "a string with a right side."

# Concatenates the two strings stored in the variables w and e.
print w + e


