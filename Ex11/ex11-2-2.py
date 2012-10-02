age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")


age = age if age is not '' else '35'
height = height if height is not '' else "6'2\""
weight = weight if weight is not '' else '180lbs'


print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
