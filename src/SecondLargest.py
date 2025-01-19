numbers = [2, 3, 7, 8, 5, 9, 12, 10]

numbers_len = len(numbers)

first_largest = second_largest = -1

i=0

while i < numbers_len:
    if numbers[i] > first_largest:
        second_largest = first_largest
        first_largest = numbers[i]
    elif numbers[i] > second_largest & numbers[i] < first_largest:
        second_largest = numbers[i]
    i+=1

print(f"Second Largest : {second_largest}")