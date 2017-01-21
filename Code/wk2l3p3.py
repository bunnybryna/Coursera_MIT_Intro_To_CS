mys = 'hello'
for char in mys:
    print char
print 'done'

greeting = 'Hello!'
count = 0
for i in greeting:
	count += 1
	if count % 2 == 0:
	    print i
	print i
print 'done'
# it will print out Heelllo!!done

school = 'Massachusetts Institute of Techonology'
numVowels = 0
numCons = 0
for i in school:
    if i == 'a' or i == 'e' or i == 'i' \
	    or i == 'o' or i == 'u':
            numVowels += 1
            # aaueiueoeoo,11
    elif i == 'o' or i == 'M':
	    print i
        # it will only print out M
        # because o fits if category, won't be counted again under elif
    else:
        numCons -= 1
        # sschsttsInstttfTchnlgy,-25
print 'numVowels is : ' + str(numVowels)
print 'numCons is : ' + str(numCons)
