numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_of_none = numbers.index(None)
summa = sum(numbers[:index_of_none]+numbers[index_of_none+1:])
numbers[4] = summa/len(numbers)

print("Измененный список:", numbers)
