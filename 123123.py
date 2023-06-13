from random import *
print('Игра "Угадай число"')
for u in range(3):
    a = int(input('Введи число от 1 до 10 >>> '))
    i = randint(1, 10)
    if a==i:
        print('|Вы угадали число')
    else:
        print('|Вы не угадали загаданное число')
print('|Загаданное число было:', i)


