def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [1, 2, 3, 4]
print("Product:", multiply_list(numbers))
