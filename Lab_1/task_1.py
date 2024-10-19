numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
o=0
summ=0
# TODO заменить значение пропущенного элемента средним арифметическим


for i in range(len(numbers)):
    if type(numbers[i]) != type(None):
        summ = summ + numbers[i]
    else:
        o=i


summ=summ/len(numbers)
numbers[o]=summ


print("Измененный список:", numbers)