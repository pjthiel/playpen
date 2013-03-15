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

def fibonacci(n):
	"""Fibonacci generator for sequence values < n."""
	a, b = 0, 1
	while True:
		if a >= n: return
		yield a
		a, b = b, a + b

@print_timing
def sum_even_fibonacci(n):
	"""Quick test of the fibonacci generator."""
	return sum(x for x in fibonacci(n) if x % 2 == 0)

@print_timing
def fibonacci_combined(n):
	"""Building on the generator, can make this a single function."""
	a, b, sum = 0, 1, 0
	while a < n:
		if a % 2 == 0:
			sum += a
		a, b = b, a + b
	return sum

print sum_even_fibonacci(4000000)
print fibonacci_combined(4000000)
