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
def multiples_3_5(n):
	total = 0
	for i in xrange(1, n + 1):
		if (i % 3 == 0) or (i % 5 == 0):
			total += i
	return total

@print_timing
def faster_multiples_3_5(t):
	t += 1
	return sum(range(3,t,3)) + sum(range(5,t,5)) - sum(range(15,t,15))

def sum_multiple(t, m):
	"""Sum of multiples based on forumla for sum of consecutive numbers:
	Fn = n(n + 1) / 2."""
	n = t / m
	return m * (n * (n + 1)) / 2

@print_timing
def fastest_multiples_3_5(t):
	return sum_multiple(t, 3) + sum_multiple(t, 5) - sum_multiple(t, 15)


x = multiples_3_5(999)
y = faster_multiples_3_5(999)
z = fastest_multiples_3_5(999)
