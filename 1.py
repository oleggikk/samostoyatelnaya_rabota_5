flag = True
while flag:
    try:
        A = int(input('Введите поочередно целые положительные числовые значения А, B, C, D, каждый с новой строки: \n'))
        B = int(input())
        C = int(input())
        D = int(input())
    except ValueError:
        print('Введите поочередно ЦЕЛЫЕ ПОЛОЖИТЕЛЬНЫЕ ЧИСЛОВЫЕ значения А, B, C, D, каждый с новой строки: ')
    else:
        if (A > 0) and (B > 0) and (C > 0) and (D > 0):
            flag = False
        else:
            print('Одно или все значения A B C D меньше или равно нулю. Ошибка.')
maxAB = max(A, B)
maxCD = max(C, D)
minAB = min(A, B)
minCD = min(C, D)
if (maxAB < maxCD) and (minAB < minCD):
    print('Прямоугольник со сторонами AB может разместиться внутри прямоугольника CD')
else:
    print('Прямоугольник со сторонами AB НЕ может разместиться внутри прямоугольника CD')