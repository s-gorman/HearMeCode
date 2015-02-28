#Lesson 2, Goal 1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly."""

"""bread = 7
jelly = 2
pb = 6
b = bread/2
number = 0
if  bread >= 2 and jelly >= 1 and pb >=1:
    while bread and jelly >= 1 and pb >= 1:
        number = number+1
        print "Making sandwich #{0}".format(number)
        bread = bread-2
        jelly = jelly-1
        pb = pb-1
else: print "Shopping time!" """

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

bread = 6
jelly = 7
pb = 3
b = bread/2
number = 0
if  bread >= 2 and jelly >= 1 and pb >=1:
    while bread and jelly >= 1 and pb >= 1:
        number = number+1
        print "Making sandwich #{0}".format(number)
        bread = bread-2
        jelly = jelly-1
        pb = pb-1
        if bread < 2 and jelly < 1 and pb < 1:
            print "Time to buy bread, peanut butter and jelly"
        elif bread < 2 and pb < 1:
            print "Time to buy bread and peanut butter"
        elif pb < 1 and jelly < 1:
            print " Time to buy peanut butter and jelly"
        elif bread < 2 and jelly < 1:
            print "Time to buy bread and jelly"
        elif jelly < 1:
            print "Time to buy jelly"
        elif bread < 2:
            print "Time to buy bread"
        elif pb < 1:
            print "Time to buy pb"
        else:
            print "I have enough bread for {0}, enough jelly for {1}, enough peanut butter for {2} more." .format(bread, jelly, pb)
else: print "Shopping time!"

#In colloboration with Hemi Kim
