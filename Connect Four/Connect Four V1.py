import time
from colorama import Fore
import pyfiglet

print(f'Welcome!')

time.sleep(1)

print(f'Connect Four is starting!')

time.sleep(1.5)


# Проверка дали всички позиции не са заети и няма къде да се постави
def connect_four_game():
    figures_dictionary = {
        "blank_space": "□",
        "first_player": "⚪",
        "second_player": "⚫"
    }

    playing_field = [[figures_dictionary["blank_space"] for el in range(7)] for row in range(6)]

    current_player_index = 0

    def win_check():
        for row in playing_field:  # Rows Checking
            current_element = row[0]
            current_counter = 1
            for index in range(1, len(row)):
                if row[index] == current_element:
                    current_counter += 1
                    if current_counter == 4 and current_element != figures_dictionary["blank_space"]:
                        return True

                else:
                    current_element = row[index]
                    current_counter = 1

        for index in range(0, len(playing_field[0])):  # Columns Checking
            current_element = playing_field[0][index]
            current_counter = 1
            for xedni in range(1, len(playing_field)):
                if playing_field[xedni][index] == current_element:
                    current_counter += 1
                    if current_counter == 4 and current_element != figures_dictionary["blank_space"]:
                        return True
                else:
                    current_element = playing_field[xedni][index]
                    current_counter = 1

        middle_index_row = 0
        middle_index_column = 0

        while middle_index_row < len(playing_field) and middle_index_column < len(playing_field[0]):  # left upper to right lower diagonal
            current_diagonal_indexes = []
            middle_index_row += 1
            middle_index_column += 1

            current_row = middle_index_row - 1
            current_column = middle_index_column
            while current_column > 0 and current_row < len(playing_field):
                current_column -= 1
                current_row += 1
                if current_row == len(playing_field):
                    break
                current_diagonal_indexes.insert(0, [current_row, current_column])

            current_row = middle_index_row
            current_column = middle_index_column - 1
            while current_row > 0 and current_column < len(playing_field[0]):
                current_row -= 1
                current_column += 1
                if current_column == len(playing_field[0]):
                    break
                current_diagonal_indexes.append([current_row, current_column])

            current_diagonal_elements = []
            for lst in current_diagonal_indexes:
                current_diagonal_elements.append(playing_field[lst[0]][lst[1]])

            if f'{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}' in "".join(current_diagonal_elements):
                return True
            elif f'{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}' in "".join(current_diagonal_elements):
                return True

        middle_index_row = len(playing_field)
        middle_index_column = len(playing_field[0])

        while middle_index_row > 0 and middle_index_column > 0:  # right lower to left upper diagonal
            current_diagonal_indexes = []
            middle_index_row -= 1
            middle_index_column -= 1

            current_row = middle_index_row + 1
            current_column = middle_index_column
            while current_row > 0 and current_column < len(playing_field[0]):
                current_row -= 1
                current_column += 1
                if current_column == len(playing_field[0]):
                    break
                current_diagonal_indexes.insert(0, [current_row, current_column])

            current_row = middle_index_row
            current_column = middle_index_column + 1
            while current_row < len(playing_field) and current_column > 0:
                current_row += 1
                current_column -= 1
                if current_row == len(playing_field):
                    break
                current_diagonal_indexes.append([current_row, current_column])

            current_diagonal_elements = []
            for lst in current_diagonal_indexes:
                current_diagonal_elements.append(playing_field[lst[0]][lst[1]])

            if f'{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}' in "".join(current_diagonal_elements):
                return True
            elif f'{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}' in "".join(current_diagonal_elements):
                return True

        middle_index_row = len(playing_field)
        middle_index_column = -1

        while middle_index_row - 1 > 0 and middle_index_column + 1 < len(playing_field[0]):  # lower left to upper right
            current_diagonal_indexes = []
            middle_index_row -= 1
            middle_index_column += 1

            current_row = middle_index_row - 1
            current_column = middle_index_column
            while True:
                current_row += 1
                current_column += 1
                if current_row == len(playing_field) or current_column == len(playing_field[0]):
                    break
                current_diagonal_indexes.insert(0, [current_row, current_column])

            current_row = middle_index_row
            current_column = middle_index_column + 1
            while True:
                current_row -= 1
                current_column -= 1
                if current_column == -1 or current_row == -1:
                    break
                current_diagonal_indexes.append([current_row, current_column])

            current_diagonal_elements = []
            for lst in current_diagonal_indexes:
                current_diagonal_elements.append(playing_field[lst[0]][lst[1]])

            if f'{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}' in "".join(current_diagonal_elements):
                return True
            elif f'{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}' in "".join(current_diagonal_elements):
                return True

        middle_index_row = -1
        middle_index_column = len(playing_field[0])

        while middle_index_row + 1 < len(playing_field) and middle_index_column - 1 > 0:  # upper right to lower left
            current_diagonal_indexes = []
            middle_index_row += 1
            middle_index_column -= 1

            current_row = middle_index_row + 1
            current_column = middle_index_column
            while True:
                current_row -= 1
                current_column -= 1
                if current_row == -1 or current_column == -1:
                    break
                current_diagonal_indexes.insert(0, [current_row, current_column])

            current_row = middle_index_row
            current_column = middle_index_column - 1
            while True:
                current_row += 1
                current_column += 1
                if current_column == len(playing_field[0]) or current_row == len(playing_field):
                    break
                current_diagonal_indexes.append([current_row, current_column])

            current_diagonal_elements = []
            for lst in current_diagonal_indexes:
                current_diagonal_elements.append(playing_field[lst[0]][lst[1]])

            if f'{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}{figures_dictionary["first_player"]}' in "".join(current_diagonal_elements):
                return True
            elif f'{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}{figures_dictionary["second_player"]}' in "".join(current_diagonal_elements):
                return True

    while True:
        if current_player_index % 2 == 0:
            selected_column = int(input("Player 1, enter the column that you wish to select: (1) "))

        else:
            selected_column = int(input("Player 2, enter the column that you wish to select: (2) "))

        for index in range(5, -1, -1):
            if playing_field[index][selected_column - 1] == figures_dictionary["blank_space"]:
                playing_field[index][selected_column - 1] = figures_dictionary["first_player"] if current_player_index % 2 == 0 else figures_dictionary["second_player"]
                print(f'Player 1 successfully put his number on position {index} {selected_column - 1}!' if current_player_index % 2 == 0 else f'Player 2 successfully put his number on position {index} {selected_column - 1}!')
                break

        else:
            print(f'The whole column is occupied!')
            current_player_index -= 1

        the_game_is_won = win_check()

        if the_game_is_won:
            print(f'GAME OVER!')
            return "Еди кой си спечели играта..."

        for row in playing_field:
            print(" ".join(row))

        current_player_index += 1


current_game_result = connect_four_game()

# Отпечатай резултата на играчите
