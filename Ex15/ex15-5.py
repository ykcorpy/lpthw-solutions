print "Type the filename:"
filename = raw_input("> ")

txt = open(filename)

print txt.read()

# argv is better than raw_input because you specify all relevant information on the command line. This way you don't have to wait for 
# the input request to come.
