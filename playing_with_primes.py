import time

def print_timing(func):
	"""Decorator for printing function timing.
	"""
	def wrapper(*arg):
		t1 = time.time()
		res = func(*arg)
		t2 = time.time()
		print '%s took %0.3f ms to execute' % (
			func.func_name, (t2 - t1) * 1000.0)
		return res
	return wrapper

@print_timing
def slow_primes(n):
	"""Brute-force approach to generating prime numbers <= n
	"""
	pp = range(2, n + 1)
	for i in xrange(len(pp)):
		for j in xrange(2, int(n ** 0.5) + 1):
			if j != pp[i] and pp[i] % j == 0:
				pp[i] = 0
	return filter(None, pp)

@print_timing
def faster_primes(n):
	"""Faster approach (using a number sieve) to generating prime numbers <= n.
	"""
	pp = range(n + 1)
	for next in xrange(2, n + 1):
		if next ** 2 >= n:
			return filter(lambda k: k > 1, pp)
		if next > 0 :
			pp[2 * next::next] = [0] * ((n // next) -1)


x = slow_primes(1000)
y = faster_primes(1000)
print len(x)
print len(y)
