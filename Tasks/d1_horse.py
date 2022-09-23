def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    start_point = (0, 0)
    current_point = [start_point, start_point]    # клетки достигнутые в результате последнего хода
    past_point = set(start_point)                 # клетки, в которых конь уже побывал
    shifts = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]  # набор смещений, обеспечивающий
    task = []                                                                          # все ходы конем из данной клетки

    """ Функция, которая совершает набор всех возможных ходов из данной клетки.
        И помещает точку или в набор текущих, или в набор, достигших цели. """

    def main_move(point_):
        moves = []
        for shift in shifts:
            move = (point_[0] + shift[0], point_[1] + shift[1])
            if move[0] == point[0] and move[1] == point[1]:
                task.append(move)
                break
            if 0 < move[0] < shape[0] and 0 < move[1] < shape[1]:
                moves.append(move)
                print(f"moves=>{moves}")
        return moves

    """ Внешний цикл проверяет сколько точек осталось после последнего хода: стартовая точка остается
         одна, когда остальные вышли за пределы поля или поместились в набор, достигших цели.
        Внутрений цикл, перебирает набор последних точек и для каждой вызывает функцию, совершающую
                  набор ходов."""

    while not len(current_point) == 1:
        storage_new_point = []    # сюда помещаются все последние точки
        for point in current_point:
            temp = main_move(point)
            storage_new_point.extend(temp)
        storage_new_point = set(storage_new_point)  # чтобы исключить повторы,приводим к типу множество
        intersect = storage_new_point.intersection(past_point)
        storage_new_point = storage_new_point - intersect   # исключаем посещенные ранее клетки
        past_point.update(storage_new_point)         # пополняем набор посещенных клеток
        storage_new_point = list(storage_new_point)
        current_point = storage_new_point   # создаем новый набор последних точек
        print(f"current_point=>{current_point}")
        print(f"task => {task}")
    return task

if __name__ == "__main__":
    res = calculate_paths((4, 4), (2, 1))
    print(f"res =>{len(res)}")