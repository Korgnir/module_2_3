my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Дан список чисел:', my_list)
print('Нужно выписывать из этого списка только положительные числа до тех пор, '
      'пока не встретите отрицательное или не закончится список: ')
positive_my_list = []
for num in my_list:
    if num > 0:
        positive_my_list.append(num)
a = len(positive_my_list)
b = 0
while a > b:
    number = int(input())
    b += 1
    if number in my_list and number > 0: # - число относится к списку и положительно
        my_list.remove(number)
    elif number in my_list:
        print('число относится к списку, но отрицательно')
        b -= 1
        continue
    else:
        print('Число не отвечает условиям')
        break
if a == b:
    print('Well done!')