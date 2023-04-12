def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 21
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return left

def sort_nums(nums):
    return sorted(nums)

user_input = input("Введите последовательность чисел через пробел: ")
nums = user_input.split()
try:
    nums = [int(num) for num in nums]
except ValueError:
    print("В последовательности должны быть только числа!")
else:
    target = input("Введите любое число: ")
    try:
        target = int(target)
    except ValueError:
        print("Введите корректное число!")
    else:
        sorted_nums = sort_nums(nums)
        index = binary_search(sorted_nums, target)
        if index == len(sorted_nums):
            print("Число больше всех элементов в последовательности!")
        elif sorted_nums[index] == target:
            print(f"Число {target} уже есть в последовательности!")
        else:
            print(f"Число {target} должно быть вставлено на позицию {index} между элементами {sorted_nums[index-1]} и {sorted_nums[index]} в отсортированной последовательности.")
