from sys import argv

script, filename = argv
print "The python script is called:%r" % script

print "We're going to print the contents of the file: %r " % filename

raw_input("Hit ENTER to continue or CTRL-C to cancel!")

content = open(filename)

print "\n", content.read()

content.close()
