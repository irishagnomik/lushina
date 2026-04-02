import random
def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1 # Если элемент не найден

random_numbers=[random.randint(1, 100) for _ in range(100)]
print(random_numbers)
with open('search_results.txt', 'w', encoding='utf-8') as f:
    f.write(str(random_numbers)+'\n')
for j in range(5):
    x=random.randint(1, 100)
    y=linear_search(random_numbers, x)
    print(f'Индекс элемента со значением {x} - {y}' if y!=-1 else f'Число {x} в списке отутсвует')
    with open('search_results.txt', 'a', encoding='utf-8') as f:
        f.write(f'Индекс элемента со значением {x} - {y}\n' if y!=-1 else f'Число {x} в списке отутсвует\n')
        