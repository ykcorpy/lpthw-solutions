from sys import argv

script, language, version = argv

print "Your script is called:", script
print "Written in:", language
print "Script version:", version

fav_color = raw_input("What is your favourite color?")
fav_number = int(raw_input("What is your favourite number?"))

print "So, your favourite color is %s and your favourite number is %d." %(fav_color, fav_number)
