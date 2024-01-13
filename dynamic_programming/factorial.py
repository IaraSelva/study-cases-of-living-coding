# recursion way

def fact(n):
    if n == 1: 
        return 1
    else:
        return n*fact(n-1)
    
# memoization - top-down approach 
def factDynamic(n, table = None):
    table = {} if table is None else table
    if n in table:
        return table[n]
    if(n == 1):
        return 1
    else:
        table[n] = n*factDynamic(n-1, table)
    return table[n]

print(fact(999))
print("\n")
print(factDynamic(900))
 

    
