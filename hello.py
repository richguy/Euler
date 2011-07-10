def fib(n):
          """Print a Fibonacci series up to n."""
          a, b = 0, 1
          seq = []
          while a < n:
              if a%2 == 0:
                seq.append(a)
              a, b = b, a+b
          return seq

print fib(4000000)