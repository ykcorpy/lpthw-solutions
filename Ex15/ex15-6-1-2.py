from sys import argv

filename = argv[1]
txt = open(filename, 'a')

txt.write("Hello world!")
txt.close()

print "Here is your file %r:" % filename

txt_again = open(filename)
print txt_again.read()
