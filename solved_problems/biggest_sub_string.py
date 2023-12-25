def max_subs(str):
    substr = set()
    left = 0
    max = 0

    for right in range(len(str)):
        if not str[right] in substr:
            substr.add(str[right])
            max = len(substr) if len(substr) > max else max
        else: 
            while str[right] in substr:
                substr.remove(str[left])
                left += 1
            substr.add(str[right])
    return max, substr

print(max_subs("abacdebadf"))


        