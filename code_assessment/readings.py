def sum_nums(num):
    soma = 0

    for digit in str(num):
        soma += int(digit)
    if soma > 9:
        sum_nums(soma)
    return soma

def readings(numbers):
    num_count = {}
    num_max_occur = 0
    count_max_occur = 0

    for num in numbers:
        digits_sum = sum_nums(num)
        n_occur = num_count.get(digits_sum, 0) + 1

        num_count[digits_sum] = n_occur

        if n_occur > count_max_occur:
            count_max_occur = n_occur
        
            if digits_sum > num_max_occur:
                num_max_occur = digits_sum
    
    return num_max_occur


numbers = [123, 456, 789, 101]
print(readings(numbers))

numbers = [123, 456, 789, 101, 200, 110]
print(readings(numbers))
