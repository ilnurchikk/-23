
#############################1Пользователь вводит с клавиатуры целое шестизначное число

# a = str(input("программа определяет,является ли введенное число — счастливым \n напишите число:"))
# b = int(a[0])+int(a[1])+int(a[2])
# c = int(a[3])+int(a[4])+int(a[5])
# if b == c:
#   print('Счастливый')
# else:
#   print('Несчастливый')
##################2Пользователь вводит Например, 723895 должно превратиться в 593827

#i = str(input("Введите шестизначное число:"))
#if len(i) != 6:
#    print(" Введите шестизначное число!!!")
#else:
#    a = int(i[0])
#    b = int(i[5])
#    p = str(b) + i[1:5] + str(a)

#print("Полученное число:", p)
####################3номер месяца
# a = int(input("Введите номер месяца:"))
#
# print(["Winter", "Spring", "Summer", "Autumn"][a % 12 // 3])
#
a = ['winter', 'spring', 'summer', 'autumn']
b = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
c = int(input("Введите месяц по номеру "))
if c == 1 or c == 12 or c == 2:
        print(b.get(1))
        print(a[0])
elif c == 3 or c == 4 or c == 5:
    print(b.get(2))
    print(a[1])
elif c == 6 or c == 7 or c == 8:
    print(b.get(3))
    print(a[2])
elif c == 9 or c == 10 or c == 11:
    print(b.get(4))
    print(a[3])
else:
    print("Такого месяца не существует")

