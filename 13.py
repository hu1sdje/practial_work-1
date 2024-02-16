import math
radius1 = int(input('Введите значение радиуса '))
radius2 = int(input('Введите значение радиуса '))
territory = (radius1 ** 2) * math.pi - (radius2 ** 2) * math.pi \
    if radius1 > radius2 else (radius2 ** 2) * math.pi - (radius1 ** 2) * math.pi
print(f'Территорияя дальности приёма: {territory}')
