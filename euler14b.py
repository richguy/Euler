def next(n):
    if n % 2:
        return 3 * n + 1
    else:
        return n / 2
 
class ChainCache:
    def __init__(self):
        self.cache = {}
 
    def __call__(self, n):
        if n == 1:
            return 1
        elif n in self.cache:
            return self.cache[n]
        else:
            c = self.__call__(next(n))
            self.cache[n] = c + 1
            return c + 1
 
chainlen = ChainCache()
 
def maxlen(x):
    m = 0
    v = 0
    for i in range(1, x):
        l = chainlen(i)
        if l > m:
            m = l
            v = i
    return v, m
 
print(maxlen(1000000))
