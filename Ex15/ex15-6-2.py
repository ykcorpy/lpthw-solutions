from sys import argv
filename = argv[1]

# Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
fo = open(filename, 'w')

a = ["Python is awesome!\n","Hello world!\n"]


fo.writelines(a)

fo.close()

fo_again = open(filename, 'r')

print fo_again.read()

fo.close()
