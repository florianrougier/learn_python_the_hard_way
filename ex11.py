print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

# here is just to test the behaviour of the input() function
# Does this function actually change the input type ?
test = input()
print type(test)

print "You are %r years old, %r tall, %r heavy" % (age, height, weight)
