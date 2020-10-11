graph = {}
graph['start'] = {'a': 5, 'b': 2}
graph['a'] = {'c': 4, 'd': 2}
graph['b'] = {'a': 6, 'd': 7}
graph['c'] = {'d': 6, 'finish': 3}
graph['d'] = {'finish': 1}
graph['finish'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['finish'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['finish'] = None

passed = []

def most_chip_node():
    chipest_node = None
    last_cost = float('inf')
    for node in costs:
        if costs[node] < last_cost and node not in passed:
            last_cost = costs[node]
            chipest_node = node
    return chipest_node


def find_shortest():
    node = most_chip_node()
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        passed.append(node)
        node = most_chip_node()
    print(parents)


if __name__ == '__main__':
    find_shortest()
