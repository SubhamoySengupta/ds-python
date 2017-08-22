# Iterator objects

#1 Generating function
def genItems(seq):
	for item in seq:
		yield item * 3

iter1 = genItems(xrange(5))

genexp = (i * 3 for i in range(10))