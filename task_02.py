def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1 # Если элемент не найден

list = [5, 10, 15, 20, 25, 30, 35, 40]
target = 35
print("Индекс элемента:", linear_search(list, target))  

# Алгорит линейный, без вложеных циклов, поэтому:
# Временная сложность  O(8), по количеству элементов в списке
# Пространственная сложность O(1), так как количество дополнительной памяти каждый раз постоянное