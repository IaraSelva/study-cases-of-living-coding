def mySqrt(x):
    if x == 0: return 0
    if x == 1: return 1
    if x < 0: return None

    left = 0
    right = x
    
    while (right-left) > 1:
        middle = int((right+left)/2) # if size % 2 == 0 else (size-1)/2
        if middle*middle > x:
            right = middle
        else: left = middle
    return left