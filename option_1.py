"""Данное решение находит все уникальные наборы троек элементов из заданного списка nums, 
   где произведение элементов в каждой тройке равно нулю."""

def find_triplets(nums):
    result = []
    n = len(nums)
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k:
                    if nums[i] * nums[j] * nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
    
    return result

nums = [1, 2, 0, 3, 0, 4]
result = find_triplets(nums)
print(result)