numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
without_none = numbers[0:4] + numbers[5:21]
sum_of_numbers = sum(without_none)
count_of_numbers = len(numbers)
average = sum_of_numbers / count_of_numbers
numbers[4] = average
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
