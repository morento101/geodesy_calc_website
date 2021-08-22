from flask.scaffold import F


def coma_replace(s):
    return s.replace(',', '.')


def y_value_for_zones(zone, distance, direction):
    if type(zone) != int:
        raise TypeError("Зона повинна бути цілим додатнім числом")
    elif type(distance) not in [int, float]:
        raise TypeError("Відстань може бути лише цілим або дробовим додатнім числом")
    elif type(direction) != str:
        raise TypeError("Запишіть напрям текстом")
    else:
        if zone <= 0:
            raise ValueError('Зона може бути лише додатньою')
        elif distance <= 0 or distance > 999_999:
            raise ValueError('Відстань може бути лише додатньою та не більшою ніж 999 999')
        elif direction.lower() not in ['захід', "схід"]:
            raise ValueError("Введіть 'захід' або 'схід'")
        else:
            if zone > 30:
                zone -= 30
            if direction.lower() == "захід":
                y_value = (zone * 1_000_000) + 500_000 - distance
                res = f"\nЗначення Ординати = {zone} * {1_000_000} + 500 000 - {distance} = {y_value}"
            else:
                y_value = (zone * 1_000_000) + 500_000 + distance
                res = f"\nЗначення Ординати = {zone} * {1_000_000} + 500 000 + {distance} = {y_value}"
    return res


def accuracy_of_scale(scale):
    if type(scale) != int:
        raise TypeError('Масштаб повинен бути цілим додатнім числом')
    elif scale <= 0:
        raise ValueError('Масштаб не може бути меньшим за нуль або дорівнювати йому')
    else:
        accuracy = scale / 10000
        res = f'\nТочність масштабу = {scale} / 10000 = {accuracy} м'
    return res


def get_scale_from_segment(segment):
    res = ''
    if type(segment) != str:
        raise TypeError('Номенклатура Повинна Бути Записана Як Текст')
    elif len(segment) <= 1:
        raise ValueError('Введенна Номенклатура Занадто Коротка')
    elif '-' not in segment and '–' not in segment:
        raise ValueError('Неправильнно Введенна Номенклатура')
    else:
        segment = segment.replace('–', '-').replace('І', 'I').replace('Х', 'X').split('-')
        is_alpha, is_digit = False, False
        for i in segment:
            if i.isalpha():
                is_alpha = True
            elif i.isdigit():
                is_digit = True
        if is_alpha and is_digit:
            roman = ('I', 'II', 'III', 'IV', 'V', 'VI',	'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
                     'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXVI', 'XXXV', 'XXXVI')
            range1_5 = (str(i) for i in range(1, 5))
            range1_145 = (str(i) for i in range(1, 145))
            range1_257 = (str(i) for i in range(1, 257))
            if segment[0].isalpha() and segment[0] not in roman:
                up_letters = ("А", "Б", "В", "Г", 'A')
                low_letters = ("а", "б", "в", "г", 'a')
                if len(segment) == 2 and segment[1].isdigit():
                    res = '1:1 000 000'
                elif len(segment) == 3 and segment[1].isdigit() and segment[2] in up_letters:
                    res = '1:500 000'
                elif len(segment) == 3 and segment[1].isdigit() and segment[2] in roman:
                    res = '1:200 000' 
                elif len(segment) == 3 and segment[1].isdigit() and segment[2] in range1_145:
                    res = '1:100 000'
                elif len(segment) == 4:
                    if segment[1].isdigit() and segment[2].isdigit() and segment[3] in up_letters:
                        res = '1:50 000'
                    else:
                        flag = False
                        for i in range1_257:
                            if segment[1].isdigit() and segment[2].isdigit() and i in segment[3] and '(' in segment[3] and ')' in segment[3]:
                                res = '1:5 000' 
                                flag = True
                                break
                        if not flag:
                            raise ValueError('Неправильнно Введенна Номенклатура')
                elif len(segment) == 5:
                    if segment[1].isdigit() and segment[2].isdigit() and segment[3] in up_letters and segment[4] in low_letters:
                        res = '1:25 000'
                    else:
                        flag = False
                        for i in range1_257:
                            for j in ('а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и'):
                                if i in segment[3] and '(' in segment[3] and j in segment[4] and ')' in segment[4]:
                                    res = '1:2 000'
                                    flag = True
                                    break
                        if not flag:
                            raise ValueError('Неправильнно Введенна Номенклатура')
                elif (len(segment) == 6 and segment[0].isalpha() and 
                segment[1].isdigit() and segment[2] in range1_145 and segment[3] in up_letters and segment[4] in low_letters and segment[5] in range1_5):
                      res = '1:10 000'
                else:
                    raise ValueError('Неправильнно Введенна Номенклатура')
            elif segment[0] in roman:
                res = '1:300 000'
            else:
              raise ValueError('Неправильнно Введенна Номенклатура')  
        else:
            raise ValueError('Неправильнно Введенна Номенклатура')
    return res


def divide_scales(dividing_scale, divider_scale):
    if type(dividing_scale) != str:
        raise TypeError("Масштаб Діленної Трапеції Повинен Бути Типу Текст")
    elif type(divider_scale) != str:
        raise TypeError("Масштаб Трапеції-Дільника Повинен Бути Типу Текст")
    elif len(dividing_scale) <= 4:
        raise ValueError('Масштаб Діленної Трапеції Повиннен Бути Мінімум Завдовжки 4 Символи')
    elif len(divider_scale) <= 4:
        raise ValueError('Масштаб Трапеції-Дільника Повиннен Бути Мінімум Завдовжки 4 Символи')
    else:
        dividing_scale, divider_scale = dividing_scale.replace(' ', ''), divider_scale.replace(' ', '')
        if dividing_scale == "1000000" and divider_scale == "500000":
            res = 4
        elif dividing_scale == "1000000" and divider_scale == "300000":
            res = 9
        elif dividing_scale == "1000000" and divider_scale == "200000":
            res = 36
        elif dividing_scale == "1000000" and divider_scale == "100000":
            res = 144
        elif dividing_scale == "100000" and divider_scale == "50000":
            res = 4
        elif dividing_scale == "50000" and divider_scale == "25000":
            res = 4
        elif dividing_scale == "25000" and divider_scale == "10000":
            res = 4
        elif dividing_scale == "100000" and divider_scale == "5000":
            res = 256
        elif dividing_scale == "5000" and divider_scale == "2000":
            res = 9
        else:
            raise ValueError('Введенні Дані Не Є Правильними')
        return res


def convert_grad_min_secs_to_decimal(string):
    if type(string) != str:
        raise TypeError('Градуси Повинни Юути Записані Як Текст')
    elif len(string) < 1:
        raise ValueError('Введіть Градуси')
    for i in string:
        if i.isalpha():
            raise ValueError('Градуси Не Можуть Вміщати В Собі Букви')
    else: 
        string = string.split(' ')
        decimal_degrees = 0
        if len(string) == 3:
            degrees, minutes, seconds = string[0], string[1], string[2]
            degrees, minutes, seconds = float(coma_replace(degrees)), float(coma_replace(minutes)), float(coma_replace(seconds))
            if float(degrees) > 0:
                decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
                decimal_degrees = round(decimal_degrees, 3)
            elif float(degrees) < 0:
                decimal_degrees = degrees - (minutes / 60) - (seconds / 3600)
                decimal_degrees = round(decimal_degrees, 3)
            elif str(degrees) == '0.0':
                decimal_degrees = 0 + (minutes / 60) + (seconds / 3600)
                decimal_degrees = round(decimal_degrees, 3)
            elif str(degrees) == '-0.0':
                decimal_degrees = 0 - (minutes / 60) - (seconds / 3600)
                decimal_degrees = round(decimal_degrees, 3)
        elif len(string) == 2:
            degrees, minutes = string[0], string[1]
            degrees, minutes = float(coma_replace(degrees)), float(coma_replace(minutes))
            if float(degrees) > 0:
                decimal_degrees = degrees + (minutes / 60)
                decimal_degrees = round(decimal_degrees, 3)
            elif float(degrees) < 0:
                decimal_degrees = degrees - (minutes / 60)
                decimal_degrees = round(decimal_degrees, 3)
            elif str(degrees) == '0.0':
                decimal_degrees = 0 + (minutes / 60)
                decimal_degrees = round(decimal_degrees, 3)
            elif str(degrees) == '-0.0':
                decimal_degrees = 0 - (minutes / 60)
                decimal_degrees = round(decimal_degrees, 3)
        elif len(string) == 1:
            degrees = string[0]
            degrees = float(coma_replace(degrees))
            decimal_degrees = round(decimal_degrees, 3)
        else:
            print('НЕПРАВИЛЬНИЙ ФОРМАТ!!!')

        return round(decimal_degrees, 3)


def scale_from_size(b, l):
    if type(b) != str:
        raise TypeError('ΔВ Повинен Бути Текстом')
    elif type(l) != str:
        raise TypeError('ΔL Повинен Бути Текстом')
    elif len(b) < 1:
        raise ValueError('ΔВ Занадто Короткий')
    elif len(l) < 1:
        raise ValueError('ΔL Занадто Короткий')
    else:
        res = ''
        b, l = convert_grad_min_secs_to_decimal(b), convert_grad_min_secs_to_decimal(l)
        if b == 4.00 and l == 6.00:
            res = '1:1 000 000'
        elif b == 2.00 and l == 3.00:
            res = '1:500 000'
        elif b == 1.333 and l == 2.00:
            res = '1:300 000'
        elif b == 0.667 and l == 1.00:
            res = '1:200 000'
        elif b == 0.333 and l == .50:
            res = '1:100 000'
        elif b == .167 and l == .25:
            res = '1:50 000'
        elif b == .083 and l == .125:
            res = '1:25 000'
        elif b == .042 and l == .062:
            res = '1:10 000'
        elif b == .021 and l == .031:
            res = '1:5 000'
        elif b == .007 and l == .010:
            res = '1:2 000'
        else:
            raise ValueError('Введені Не Правилі Розміри Рамки')
        return res
