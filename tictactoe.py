def define_winner(cell: list) -> str:
    rows = [[cell[0], cell[1], cell[2]], [cell[3], cell[4], cell[5]], [cell[6], cell[7], cell[8]]]
    columns = [[cell[0], cell[3], cell[6]], [cell[1], cell[4], cell[7]], [cell[2], cell[5], cell[8]]]
    diagonal = [[cell[0], cell[4], cell[8]], [cell[2], cell[4], cell[6]]]
    only_x = ['X', 'X', 'X']
    only_o = ['O', 'O', 'O']
    if abs(cell.count('X') - cell.count('O')) > 1:
        return 'Impossible'
    if (rows[0] == only_x) or (rows[1] == only_x) or (rows[2] == only_x):
        if (rows[0] == only_o) or (rows[1] == only_o) or (rows[2] == only_o):
            return 'Impossible'
        else:
            return 'X wins'
    if (columns[0] == only_x) or (columns[1] == only_x) or (columns[2] == only_x):
        if (columns[0] == only_o) or (columns[1] == only_o) or (columns[2] == only_o):
            return 'Impossible'
        else:
            return 'X wins'
    if (rows[0] == only_o) or (rows[1] == only_o) or (rows[2] == only_o):
        if (rows[0] == only_x) or (rows[1] == only_x) or (rows[2] == only_x):
            return 'Impossible'
        else:
            return 'O wins'
    if (columns[0] == only_o) or (columns[1] == only_o) or (columns[2] == only_o):
        if (columns[0] == only_x) or (columns[1] == only_x) or (columns[2] == only_x):
            return 'Impossible'
        else:
            return 'O wins'
    if (diagonal[0] == only_x) or (diagonal[1] == only_x):
        return 'X wins'
    if (diagonal[0] == only_o) or (diagonal[1] == only_o):
        return 'O wins'
    if cell.count(' ') == 0:
        if (rows[0] or rows[1] or rows[2]) or (columns[0] or columns[1] or columns[2]) or (
                diagonal[0] or diagonal[1]) != (only_o or only_x):
            return 'Draw'
    else:
        return 'Game not finished'


def get_field() -> list:
    return list(' ' * 9)


def print_field(cell: list) -> None:
    print('---------\n'
          + '| ' + cell[0] + ' ' + cell[1] + ' ' + cell[2] + ' |\n'
          + '| ' + cell[3] + ' ' + cell[4] + ' ' + cell[5] + ' |\n'
          + '| ' + cell[6] + ' ' + cell[7] + ' ' + cell[8] + ' |\n'
          + '---------')


def get_coordinates() -> str:
    print('Enter the coordinates:', end=' ')
    return input().strip()


def check_numbers(user_input: str) -> bool:
    if len(user_input) != 3:
        return False
    if user_input[1] != ' ':
        return False
    if not user_input[0].isdigit() or not user_input[2].isdigit():
        return False
    return True


def check_range(_x: int, _y: int) -> bool:
    return 1 <= _x <= 3 and 1 <= _y <= 3


def check_cell_occupied(_field: list, _coordinates: list) -> bool:
    index = (_coordinates[1] - 1) + (_coordinates[0] - 1) * 3
    return _field[index] == ' '


def cast_coordinates(_coordinates: str) -> list:
    return [int(_coordinate) for _coordinate in _coordinates.split()]


def apply_coordinates(_field: list, _coordinates: list, symbol: str) -> None:
    index = (_coordinates[1] - 1) + (_coordinates[0] - 1) * 3
    _field[index] = symbol


def run_code(symbol: str) -> bool:
    input_coordinates = get_coordinates()
    if not check_numbers(input_coordinates):
        print('You should enter numbers!')
        return False
    coordinates = cast_coordinates(input_coordinates)
    y = coordinates[0]
    x = coordinates[1]
    if not check_range(x, y):
        print('Coordinates should be from 1 to 3!')
        return False
    if not check_cell_occupied(field, coordinates):
        print('This cell is occupied! Choose another one!')
        return False
    apply_coordinates(field, coordinates, symbol)
    print_field(field)
    return True


def move_user(symbol: str) -> bool:
    while True:
        if run_code(symbol):
            break
    end_of_game = define_winner(field)
    if (end_of_game == 'X wins') or (end_of_game == 'O wins') or (end_of_game == 'Draw'):
        print(end_of_game)
        return True
    return False


field = get_field()
print_field(field)
while True:
    if move_user('X'):
        break
    if move_user('O'):
        break
