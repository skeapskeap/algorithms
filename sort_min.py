import random

num_list = [random.randint(0,100) for i in range(5)]
sorted_list = []
print(num_list)
print('='*50)

while len(num_list):
    min_num = num_list[0]
    min_idx = 0
    for idx, num in enumerate(num_list):
        if num < min_num:
            min_num = num
            min_idx = idx

    print(f'pop number {min_num} with index {min_idx}')
    print(f'num_list= {num_list}')
    print('='*50)
    sorted_list.append(num_list.pop(min_idx))

print(f'sorted_list: {sorted_list}')