from sys import argv

script, filename = argv
prompt = '> '
txt = open(filename)

print "Here's your file %r" % filename
print txt.read()

print "Type the filename again please"
filename = raw_input(prompt)

# Read the file again
txt = open(filename)
print txt.read()
