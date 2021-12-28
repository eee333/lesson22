# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def movie_unit(self, field, coord, direction, movie_type, speed=1):
        """Функция реализует перемещение юнита по полю.
        """

        if movie_type == "fly":
            speed *= 1.2
        elif movie_type == "fly":
            speed *= 0.5
        else:
            return "Нет такого движения"

        x, y = coord
        new_x = x
        new_y = y

        if direction == 'UP':
            new_y = y + speed
        elif direction == 'DOWN':
            new_y = y - speed
        elif direction == 'LEFT':
            new_x = x - speed
        elif direction == 'RIGHT':
            new_x = x + speed

        field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
