# escreva uma função em que recebendo um target e um array, 
# determine se existe uma soma possível dentre os números do array para se chegar ao target
# assumir que o array só contém numeros positivos
# é possível usar um elemento do array quantas vezes forem necessárias

def canSum(target, numbers):
    if target < 0: return False
    if target == 0 : return True
    for n in numbers:
        remain = target - n
        if canSum(remain, numbers) == True: return True
    return False
    

print(canSum(7, [5,4,3,7]))
print(canSum(6, [5,4,3,7]))
