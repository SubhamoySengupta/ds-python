def fibonacci(cnt):
	a=0
	b=1
	COUNT = 0
	while COUNT < cnt:
		yield a
		future = a + b
		a = b
		b = future
		COUNT += 1


c = fibonacci(7)