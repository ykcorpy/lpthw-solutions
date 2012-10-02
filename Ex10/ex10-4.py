# there's no need to escape 
# because it's not ambiguous or confusing there
# consider this statement: print '"'
# %s for printing and %r for debugging

stuff = "I have \"nothing\" to say to you 'dude'."
print "She said: %r" % stuff
print "She yelled: %s" % stuff




# Extra credit 10-4
# %r prints it the way you'd write it in your file
# when using %r, one thing I noticed is that every single string is delimited by single quotes

# %s prints it the way you'd like to see it

