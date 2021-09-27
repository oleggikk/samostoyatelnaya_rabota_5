A, B, C, D = int(input('Введите поочередно значения A, B, C, D: \n')), int(input()), int(input()), int(input())
maxAB = max(A, B)
maxCD = max(C, D)
minAB = min(A, B)
minCD = min(C, D)
if (maxAB < maxCD) and (minAB < minCD):
    print('Прямоугольник со сторонами AB может разместиться внутри прямоугольника CD')
else:
    print('Прямоугольник со сторонами AB НЕ может разместиться внутри прямоугольника CD')