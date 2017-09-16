a = [2,4,10,16] 
b = (a * 5)
for i in b:
    if (i % 2 == 0):
        print "number is {}. this is an even number.".format(i)
    elif (i %2 != 0):
        print "number is {}. this is an odd mumber".format(i)