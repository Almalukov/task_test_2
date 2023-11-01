"""В этой версии кода используется функция combinations из модуля itertools
   для создания всех возможных комбинаций по 3 элемента из списка nums. 
   Затем мы проверяем, содержит ли каждая комбинация хотя бы один ноль, 
   и если да, то добавляем её в результат."""

from itertools import combinations

def find_triplets(nums):
    result = [list(combo) for combo in combinations(nums, 3) if 0 in combo]
    return result

nums = [1, 2, 0, 3, 0, 4]
result = find_triplets(nums)
print(result)