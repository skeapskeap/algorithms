from collections import deque

graph = {}
graph[11] = [2, 3]
graph[2] = [4, 6]
graph[3] = [6]
graph[4] = [12]
graph[6] = [12]

def search():
    queue = deque()
    queue += graph[11]
    listed = []
    while queue:
        num = queue.popleft()
        if num in listed:
            continue
        
        if num >= 11:
            print(f'Нашелся! {num}')
            return True
        else:
            print(num)
            listed.append(num)
            print(listed)
            queue += graph[num]
    return False

search()
            