# recursive way
def fib(n):
    if (n <= 2): return 1
    return fib(n-1) + fib(n-2)
    
print(fib(0))
print(fib(1))
print(fib(20))

# memoization - top-down approach 
def fibDynamic(n, table = None):
    table = {} if table is None else table
    if n in table:
        return table[n]
    if n <= 2 : return 1
    
    table[n] = fibDynamic(n-1, table) + fibDynamic(n-2, table) 
    return table[n]

print("\n")
print(fib(0))
print(fib(1))
print(fib(30))

# tabulation bottle-up approach
def fibTab(n):
    table = [0]*(n+1)
    table[0] = 0
    table[1] = 1

    for i in range(2, len(table)):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print("\n")
print(fibTab(1))
print(fibTab(10))
print(fibTab(30))


# optimized O(1)
def fibonacci(n):
    current = 0
    left = 0
    right = 1

    for _ in range(2, n+1):
        current = left + right
        left = right
        right = current
    return left

print("\n")
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))
print(fibonacci(10000))