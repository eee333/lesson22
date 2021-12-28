# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def move(self, field, coord: list, direction, type_move: str, speed=1):
        x, y = coord
        new_y = y
        new_x = x
        if type_move == "fly":
            speed *= 1.2
        elif type_move == "crawl":
            speed *= 0.5
        if direction == 'UP':
            new_y = y + speed
        elif direction == 'DOWN':
            new_y = y - speed
        elif direction == 'LEFT':
            new_x = x - speed
        elif direction == 'RIGTH':
            new_x = x + speed

        field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
