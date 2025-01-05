def fib(n, n_fib={1:1, 2:1}):
    if n in n_fib: return n_fib[n]
    result = fib(n-1, n_fib) + fib(n-2, n_fib)
    n_fib[n] = result
    return result
    
#print(fib(1000))

# 1  2  3  4  5  6  7  8  9  10
# 1  1  2  3  5  8  13 21 34  55

def gridTraveler(m, n, paths={}):
    if m == 0 or n == 0: return 0
    if m == 1 and n == 1: return 1

    coord = str(m)+","+str(n)
    if coord in paths: return paths[coord]

    paths[coord] = gridTraveler(m-1, n, paths) + gridTraveler(m, n-1, paths)
    return paths[coord]

def getPath(m, n, paths, path):
    if m == 0 or n == 0 : return

    coord = str(m)+","+str(n)
    path.append(coord)

    if m == 1 and n == 1:
        paths.append(path)
        return
    
    getPath(m-1, n, paths, path[:])
    getPath(m, n-1, paths, path[:])

    return paths

def findPaths(m, n):
    paths = []
    getPath(m, n, paths, [])
    return len(paths), paths
'''
print(gridTraveler(2,3))
print(gridTraveler(18,18))
print(findPaths(2,3))
print(findPaths(1,1))
print(findPaths(2,2))
'''
'''
def canSum(target, values, all_sums, unique_sum):
    if target == 0: 
        all_sums.append(unique_sum)
        return
    if target < 0: return

    for i, num in enumerate(values):
        unique_sum.append(num)
        remainder = target - num
        canSum(remainder, values[i+1:], all_sums, unique_sum[:])
        unique_sum.pop()
    

def sum(target, values):
    all_sums = []

    canSum(target, values, all_sums, [])

    return len(all_sums) > 0, all_sums


print(sum(7, [2,3]))
print(sum(7, [5,3,4,7]))
print(sum(7, [2,4]))
print(sum(8, [2,3,5]))
print(sum(9, [2,7,9,5,4,3,6,1,8,7]))
print(sum(300, [7,14]))

'''

def canSum(target, values, memo=None):
    if memo is None: memo = {}
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False

    for num in values:
        remainder = target - num
        if canSum(remainder, values, memo) == True: 
            memo[target] = True
            return True
    
    memo[target] = False
    return False
'''
print(canSum(7, [2,3]))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7,14]))
'''

def howSum(target, values, memo={}):
    if target in memo: return memo[target]
    if target == 0: return [[]]
    if target < 0: return None

    all_combinations = []

    for i, num in enumerate(values):
        remain = target - num
        result = howSum(remain, values[i+1:])
        if result is not None:
            for combination in result:
                all_combinations.append(combination + [num])
    
    memo[target] = all_combinations if all_combinations else None
    return all_combinations

print(howSum(7, [2,3,4,7]))
print(howSum(300, [2,15]))
