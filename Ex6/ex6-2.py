# 1. Go through each line and list each variable that is being assigned a string. For example x, binary, and y are examples of variables being assigned strings, but hilarious is not because False doesn't have "" around it.

# 2. This is your list of strings, so now you just need to see which ones have strings being put inside them.

# 3. Go through your list of strings, and find each one that is on the right side of a + or a %.

# 4. The ones on the right of a % + are the "strings going into strings" and that's your count.



# example of a variable being assigned a string
x = "There are %d types of people." % 10

# example of a variable being assigned a string
binary = "binary"


# example of a variable being assigned a string
do_not = "don't"


# example of a variable being assigned a string
y = "Those who know %s and those who %s." % (binary, do_not)    # "strings going into strings is 2"

print x
print y

print "I said: %r." % x # "strings going into strings is 3"
print "I also said: '%s'." % y # "strings going into strings is 4"

hilarious = False


# example of a variable being assigned a string
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# example of a variable being assigned a string
w = "This is the left side of..."


# example of a variable being assigned a string
e = "a string with a right side."

print w + e # "strings going into strings is 5"
