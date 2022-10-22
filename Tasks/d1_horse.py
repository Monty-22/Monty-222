def calculate_paths(shape: (int, int), point: (int, int)) -> int:

    task_point = point
    start_point = (0, 0)
    current_point = [start_point]    # клетки достигнутые в результате последнего хода
    past_point = set(start_point)                 # клетки, в которых конь уже побывал
    shifts = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]  # набор смещений, обеспечивающий
    task = []                                                                          # все ходы конем из данной клетки

    """ Функция, которая совершает набор всех возможных ходов из данной клетки.
        И помещает точку или в набор текущих, или в набор, достигших цели. """

    def main_move(point_move):
        moves = []
        for shift in shifts:
            move = (point_move[0] + shift[0], point_move[1] + shift[1])
            if move[0] == task_point[0] and move[1] == task_point[1]:   # Проверяем не пришли ли в нужную точку
                task.append(move)
                break
            if 0 < move[0] < shape[0] and 0 < move[1] < shape[1]:    # Проверяем не вышли ли за пределы поля
                moves.append(move)
                print(f"moves=>{moves}")
        return moves

    """ Внешний цикл проверяет сколько точек осталось после последнего хода: стартовая точка остается
         одна, когда остальные вышли за пределы поля или поместились в набор, достигших цели.
        Внутрений цикл, перебирает набор последних точек и для каждой вызывает функцию, совершающую
                  набор ходов."""

    while not len(current_point) == 0:
        storage_new_point = []    # сюда помещаются все последние точки
        for point in current_point:
            temp = main_move(point)
            storage_new_point.extend(temp)
        storage_new_point = set(storage_new_point)  # чтобы исключить повторы,приводим к типу множество
        intersect = storage_new_point.intersection(past_point)
        storage_new_point = storage_new_point - intersect   # исключаем посещенные ранее клетки
        past_point.update(storage_new_point)         # пополняем набор посещенных клеток
        storage_new_point = list(storage_new_point)
        current_point = storage_new_point    # создаем новый набор последних точек

        print(f"current_point=>{current_point}")
        print(f"task => {task}")
    return task

if __name__ == "__main__":
    res = calculate_paths((10, 10), (8, 8))
    print(f"res =>{len(res)}")