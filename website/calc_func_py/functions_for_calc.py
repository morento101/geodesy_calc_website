def coma_replace(string):
    if ',' in string:
        return string.replace(',', '')


def y_value_for_zones(zone, distance, direction):
    try:
        if type(zone) != int:
            raise TypeError("Зона повинна бути цілим додатнім числом")
        elif type(distance) not in [int, float]:
            raise TypeError("Відстань може бути лише цілим або дробовим додатнім числом")
        elif type(direction) != str:
            raise TypeError("Запишіть напрям текстом")
        else:
            if zone <= 0:
                raise ValueError('Зона може бути лише додатньою')
            elif distance <= 0:
                raise ValueError('Зона може бути лише додатньою')
            elif direction not in ['захід', "схід"]:
                raise ValueError("Введіть 'захід' або 'схід'")
            else:
                zone, distance, direction = coma_replace(zone), coma_replace(distance), coma_replace(direction)
                if zone > 30:
                    zone -= 30
                if direction.lower() == "захід":
                    y_value = (zone * 1_000_000) + 500_000 - distance
                else:
                    y_value = (zone * 1_000_000) + 500_000 + distance
    except Exception as e:
        return e

    return y_value

