flag = True
while flag:
    try:
        A = int(input('Введите поочередно положительные числовые значения A, B, C, D: \n'))
        B = int(input())
        C = int(input())
        D = int(input())
    except ValueError:
        print('Введите поочередно положительные ЧИСЛОВЫЕ значения А, B, C, D, каждый с новой строки: ')
    else:
        flag = False
if (A <= 0) or (B <= 0) or (C <= 0) or (D <= 0):
    print('Одно или все значения A B C D меньше или равно нулю. Ошибка.')
if (A > 0) and (B > 0) or (C > 0) or (D > 0):
    maxAB = max(A, B)
    maxCD = max(C, D)
    minAB = min(A, B)
    minCD = min(C, D)
    if (maxAB < maxCD) and (minAB < minCD):
        print('Прямоугольник со сторонами AB может разместиться внутри прямоугольника CD')
    else:
        print('Прямоугольник со сторонами AB НЕ может разместиться внутри прямоугольника CD')