min = 0
max = 1000

num = int(input('say number between 0 and 1000:\n'))
print ('OK. GO...')
while (max-min) > 1:
    mid = (min+max)//2
    if mid == num:
        print(mid)
        break
    if num > mid:
        min = mid
    else:
        max = mid
    print(mid)