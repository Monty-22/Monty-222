import random


"Экземпляр Cell - Клетка - содержит номер ее строки и столбца, а также цену."

class Cell:
    def __init__(self, row_, column_,  price):
        self.row = row_
        self.column = column_
        self.price = price

    def __str__(self):
        return str([self.row, self.column, self.price])

    def __gt__(self, other):
        return self.price > other.price
    def __lt__(self, other):
        return self.price < other.price

"Экземпляр Move - Ход - отражает сделанный ход: клетку, куда он был совершен и ход, из которого он был сделан."
"Благодаря атрибуту prev Ход содержит в себе весь предыдущий маршрут."

class Move:
    def __init__(self, prev_move, cell):
        self.prev = prev_move
        self.cell = cell
    def __str__(self):
        return str([self.prev, self.cell])

    def __gt__(self, other):
        return self.cell > other.cell
    def __lt__(self, other):
        return self.cell < other.cell

"""Field - класс, содержащий поле, двумерная сетка, в которой происходит движение.
Само поле представляет собой список списков экземпляров Cell.
В функции __init__ заодно с инициализацией выводится массив поля в терминал."""

class Field:
    def __init__(self, row_, column_):
        self.row = row_
        self.column = column_
        self.list_row = []
        for i in range(self.row):
            list_cell = []
            for j in range(self.column):
                cell = Cell(i, j, 10)
                list_cell.append(cell)
                print(cell, end=" ")
            print("\n")
            self.list_row.append(list_cell)
        print("\n" * 2)

    " Метод check_in_field проверяет не выходит ли данное смещение из данной клетки за пределы поля?"

    def check_in_field(self, shift_, row_, column_):
        return 0 <= row_ + shift_[0] <= self.row - 1 and 0 <= column_ + shift_[1] <= self.column - 1




"Метод check_duplicat проверяет: не повторяет ли данный ход прошлые ходы маршрута ?"

def check_duplicat(move_):
    check_move = move_
    prev_move = check_move.prev
    while not prev_move is None:   # Пока не достигнем стартового хода.
        if prev_move.cell is check_move.cell:
            return True
        prev_move = prev_move.prev
    return False

"Функция делает четыре хода из стартового хода и возвращает список получившихся ходов."

def make_move(start_move, field_):
    moves = []
    i = start_move.cell.row
    j = start_move.cell.column
    if field_.check_in_field((-1, 0), i, j):   # Проверка выхода за пределы поля.
        move_top = Move(start_move, field_.list_row[i - 1][j])  # Ход вверх по полю.
        if not check_duplicat(move_top):        # Проверка на наличие хода на такую же клетку в данном маршруте.
            moves.append(move_top)
    if field_.check_in_field(( 0, 1), i, j):
        move_right = Move(start_move, field_.list_row[j][j + 1])  # Ход вправо.
        if not check_duplicat(move_right):
            moves.append(move_right)
    if field_.check_in_field((1, 0), i, j):
        move_bottom = Move(start_move, field_.list_row[i + 1][j])  # Ход вниз.
        if not check_duplicat(move_bottom):
            moves.append(move_bottom)
    if field_.check_in_field((0, -1), i, j):
        move_left = Move(start_move, field_.list_row[i][j - 1])  # Ход влево.
        if not check_duplicat(move_left):
            moves.append(move_left)
    print (f"len moves = {len(moves)}")

    return moves


def mast_function(row_, column_, start, target):
    field = Field(row_, column_) # Создаем поле.
    field.list_row[0][1].price = 1 # Для проверки назначаем дешевый маршрут
    field.list_row[0][2].price = 1
    field.list_row[0][3].price = 1
    field.list_row[1][3].price = 1
    field.list_row[2][3].price = 1

    all_routs = [] # Список со всеми маршрутами(последними ходами).
    new_moves = [] # Список со всеми получившимися ходами из каждого хода all_routs.
    succeed_routs = [] # Список маршрутов, достигших цели.
    i_start = start[0]
    j_start = start[1]
    i_target = target[0]
    j_target = target[1]
    target_cell = field.list_row[i_target][j_target] # Создаем клетку, являющуюся целью.
    start_move = Move(None, field.list_row[i_start][j_start]) # Создаем первый ход.
    all_routs.append(start_move)

    count_while = 0 # Подсчет циклов(для отладки).

    while all_routs: # Цикл продолжается, пока все ходы не достигнут цели или не выйдут за пределы поля.
        count_while += 1
        for move in all_routs:
            new_moves.extend(make_move(move, field))
        all_routs.clear()

        for move in new_moves:
            if move.cell is target_cell:
                succeed_routs.append(move)
            else:
                all_routs.append(move)
        new_moves.clear()
        print(f"count_while = {count_while}" + "\n")
    return succeed_routs


if __name__ == "__main__":

    row = column = 5
    start_point = (0, 0)
    target_point = (3, 3)
    list_routs = mast_function(row, column, start_point, target_point)
    list_routs = sorted(list_routs)
    penny_rout = list_routs[0]  # Самый дешевый маршрут.

    while penny_rout:
        print(penny_rout.cell)
        penny_rout = penny_rout.prev












