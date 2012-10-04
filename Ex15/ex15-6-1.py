filename = raw_input("Name of file to open: ")

txt = open(filename, 'a')

txt.write("Hello world!")
txt.close()

print "Here is your file %r:" % filename

txt_again = open(filename)
print txt_again.read()
