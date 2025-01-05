class Sort:
    def __init__(self, list) -> None:
        self.list = list

    def mergeSort(self, start, end):
        # divide into smaller lists
        if end - start > 1:
            mid = (start + end)//2
            self.mergeSort(start, mid)
            self.mergeSort(mid, end)
            self.merge(start, mid, end)
        return self.list

    def merge(self, start, mid, end):
        # get the values from left and right
        left = self.list[start:mid]
        right = self.list[mid:end]
        l, r = 0, 0

        for i in range(start, end):
            # check if the index arent out of range
            if r > len(right)-1:
                self.list[i] = left[l]
                l += 1
            elif l > len(left)-1:
                self.list[i] = right[r]
                r += 1
            # compare both values
            elif left[l] < right[r]:
                self.list[i] = left[l]
                l += 1
            else:
                self.list[i] = right[r]
                r += 1

sort = Sort([-7,1,25,72,19,14,33,6,18,0,5,6,27,7,-12,11,3,1,10,28,95,6])
print(sort.mergeSort(0, len(sort.list)))

def num_to_binary(num, result=""):
    if num == 0:
        return result
    
    result = str(num % 2) + result
    return num_to_binary(num//2, result)

def sum_num(num):
    if num == 0:
        return num

    return num + sum_num(num-1)

def binary_search(arr, num, left=0, right=0):
    if left == 0 and right == 0:
        right = len(arr)-1
    if left > right:
        return "non existent"

    mid = (right + left)//2

    if arr[mid] == num: return mid

    if arr[mid] > num: return binary_search(arr, num, left, mid-1)

    return binary_search(arr, num, left, mid+1)

