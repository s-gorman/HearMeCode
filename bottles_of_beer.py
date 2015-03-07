#for number in range (99):
#    print 99-number

#bo_wall = range (99, 1, -1)
#print bo_wall

#bo_wall2 = range (98, 0, -1)
#print bo_wall2

"""number = 100
number_2 = 99
verse1 = 0

for verse in range (99, 0, -1):


  if verse1 <= 99:
    number1 = number - 1
    print "{0} bottles of beer on the wall, {0} bottles of beer...".format(number1)
    number2 = number_2 - 1
    print "{0} bottles of beer on the wall".format(number2)
    verse = verse + 1
  
  else:
    stop"""

for bob in range(99, 0, -1):
        print "{0} bottles of beer on the wall, {0} bottles of beer, if one of them should happen to fall {1} bottles of beer".format(bob, bob-1)
