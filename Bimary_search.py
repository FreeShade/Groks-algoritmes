# Бінарний пошук
def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3)) # => 1 походу
print(binary_search(my_list, -1)) # => None

# def binary_search(lst, item):
#     low = 0
#     high = len(lst) - 1
    
#     while low <= high:
#         mid = (low + high) // 2  # Використовуємо цілочисельне ділення
#         guess = lst[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# my_list = [1, 3, 5, 7, 9]

# print(binary_search(my_list, 3))  # Виведе 1
# print(binary_search(my_list, -1))  # Виведе None