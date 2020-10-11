import random

array = [random.randint(0,100) for i in range(20)]
print(array)

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        base = array.pop(0)
        le = [item for item in array if (item < base or item == base)]
        gt = [item for item in array if item > base]
        print(f'base: {base}, le: {le}, gt: {gt}')
        return (quick_sort(le) + [base] + quick_sort(gt))

print(quick_sort(array))