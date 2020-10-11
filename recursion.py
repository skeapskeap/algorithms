import random

def countdown(i):
    print(i)
    if i>0:
        countdown(i-1)
    else:
        print('Booom')

def summ(some_list):
    if some_list:
        return some_list.pop(0)+summ(some_list)
    else:
        return 0
    
def length(some_list):
    if some_list:
        some_list.pop(0)
        return 1 + length(some_list)
    else:
        return 0

def max_num(some_list):
    if some_list:
        if len(some_list) == 1:
            return some_list.pop(0)
        else:
            num = some_list.pop(0)
            next_num = max_num(some_list)
            if num < next_num:
                return next_num
            else:
                return num
    else:
        return 0

def bin_search(num, min=0, max=1000):
    if (max-min) == 1:
        mid = min
        print(mid)
    else:
        mid = (min+max)//2
        print(mid)
        if mid == num:
            return mid
        if num > mid:
            return bin_search(num, min=mid, max=max)
        else:
            return bin_search(num, min=min, max=mid)

if __name__ == '__main__':
    num_list = [random.randint(0,100) for i in range(10)]
    #print(num_list)
    #countdown(5)
    #print(summ(num_list))
    #print(length(num_list))
    #print(max_num(num_list))
    print(bin_search(346, 0, 1000))