centimeteres = (float(input('Введите расстояние в сантиметрах: ')))
print(((centimeteres / 2.54) / 12) / 3, 'ярдов', (((centimeteres / 2.54) / 12) / 3) // 1760,
      'миль',(centimeteres / 2.54) // 12, 'футов', centimeteres / 2.54, 'дюймов', sep='\n')