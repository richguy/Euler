def fib(n):    # write Fibonacci series up to n
         """Print a Fibonacci series up to n."""
         a, b = 0, 1
         evens = 0
         while a < n:
             if a%2 == 0:
                evens = evens + a
             a, b = b, a+b
         return evens

print fib(4000000)