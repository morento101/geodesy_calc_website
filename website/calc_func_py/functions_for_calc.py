from flask import flash

def coma_replace(string):
    if type(string) == float:
        string = str(string)
        if ',' in string:
            string = float(string.replace(',', '.'))
    return string


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
        elif direction not in ['захід', "схід"]:
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
