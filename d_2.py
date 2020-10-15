''' в описании графа для каждого узла
есть словарь соседей со стоимостями
перехода к ним '''
graph = {}
graph['start'] = {'a': 10}
graph['a'] = {'b': 20}
graph['b'] = {'c': 1, 'finish': 30}
graph['c'] = {'a': 1}
graph['finish'] = {}

''' в эту таблицу по ходу работы
алгоритма для каждого узла вносятся
стоимости перехода к ним от начала '''
infinity = float('inf')
costs = {}
costs['a'] = 10 # сначала известны только стоимости
costs['b'] = infinity # непосредственных соседей
costs['c'] = infinity # у остальных стоимость = бесконечность
costs['finish'] = infinity

parents = {}
parents['a'] = 'start'
parents['finish'] = None

passed = [] # список уже проверенных узлов

def most_chip_node():
    chipest_node = None
    last_cost = float('inf')
    for node in costs:
        if costs[node] < last_cost and node not in passed:
            last_cost = costs[node]
            chipest_node = node
    return chipest_node


def find_shortest():
    node = most_chip_node() #начинаем с узла с наименьшей стоимостью
    while node: # пока все узлы не попадут в список passed
        cost = costs[node] # берём стоимость узла
        neighbors = graph[node] # берём список его соседей
        for n in neighbors: # вычисляем стоимость до этих соседей через node 
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]: # если она оказалсь меньше прежней
                costs[n] = new_cost # тогда новая цена пишется в словарь стоимостей
                parents[n] = node   # и node становится родителем этого соседа
        passed.append(node) # записываем node в список обработанных узлов
        node = most_chip_node() # и берём следующий узел с наименьшей стоимостью
    print(parents, costs['finish'])


if __name__ == '__main__':
    find_shortest()
