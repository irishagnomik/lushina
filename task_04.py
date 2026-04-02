import random
import os
import timeit
def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1 # Если элемент не найден

if os.path.exists('search_results.txt'):
    os.remove('search_results.txt')
random_numbers_10=[random.randint(1, 100) for _ in range(10)]
random_numbers_100=[random.randint(1, 100) for _ in range(100)]
random_numbers_1000=[random.randint(1, 100) for _ in range(1000)]
list_random=[random_numbers_10, random_numbers_100, random_numbers_1000]
for rlist in list_random:
    print(rlist)
    time_taken=0
    for j in range(5):
        x=random.randint(1, 100)
        y=linear_search(rlist, x)
        time_taken = time_taken+timeit.timeit(
            stmt='linear_search(rlist, x)',
            setup='from __main__ import linear_search, rlist, x',
            number=1000
        )
        print(f'Индекс элемента со значением {x} - {y}' if y!=-1 else f'Число {x} в списке отутсвует')
    print(f'Среднее время одного поиска в списке из {len(rlist)} элементов : {time_taken / 5*1000:.6f} секунд\n')
    
        