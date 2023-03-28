import pyfiglet
from colorama import Fore
import time

print("\n" + time.asctime())
print("\n")
first_person_symbol = '✘'
second_person_symbol = '⬤'

Welcome = pyfiglet.figlet_format("Welcome!", font="big")
print(Fore.CYAN + Welcome)
time.sleep(1.5)
tic_tac_toe = pyfiglet.figlet_format("Let's play Tic_Tac_Toe!", font="big")
print(Fore.CYAN + tic_tac_toe)
time.sleep(1.5)
the_players_want_to_play = True

do_you_know_the_rules = str(input(Fore.LIGHTWHITE_EX + "Are you familiar with the game? "))

if do_you_know_the_rules == "no" or do_you_know_the_rules == "No":
    print("\n Two players take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.")
    time.sleep(8)
    more_info = str(input("\nDo you need more explanation before starting the game? "))
    if more_info == "yes" or more_info == "Yes":
        print("\n https://www.youtube.com/watch?v=USEjXNCTvcc")
        time.sleep(15)

while the_players_want_to_play:
    first_row = ["□", "□", "□"]
    second_row = ["□", "□", "□"]
    third_row = ["□", "□", "□"]
    print("\n")
    print(Fore.LIGHTWHITE_EX + ' '.join(first_row))
    time.sleep(0.3)
    print(' '.join(second_row))
    time.sleep(0.3)
    print(' '.join(third_row))

    index = -1
    the_game_is_running = True
    game_over = pyfiglet.figlet_format("Game Over!", font="slant")

    while the_game_is_running:
        index += 1
        if index % 2 == 0:
            current_symbol = first_person_symbol
            time.sleep(0.2)
            selected_line = int(input(Fore.RED + "\nPlayer 1, choose a line:  "))
            time.sleep(0.2)
            selected_position = int(input(Fore.RED + "Player 1, choose a position: "))
            time.sleep(0.2)
            if selected_position > 3:
                print(Fore.YELLOW + "You have entered an invalid position and wasted your move!")
            else:
                if selected_line == 1:
                    if first_row[selected_position - 1] == "□":
                        first_row.insert((selected_position - 1), current_symbol)
                        first_row.pop(selected_position)
                    else:
                        print(Fore.YELLOW + "This position is already taken! You have wasted your move!")

                elif selected_line == 2:
                    if second_row[selected_position - 1] == "□":
                        second_row.insert((selected_position - 1), current_symbol)
                        second_row.pop(selected_position)
                    else:
                        print(Fore.YELLOW + "This position is already taken! You have wasted your move!")

                elif selected_line == 3:
                    if third_row[selected_position - 1] == "□":
                        third_row.insert((selected_position - 1), current_symbol)
                        third_row.pop(selected_position)
                    else:
                        print(Fore.YELLOW + "This position is already taken! You have wasted your move!")

                else:
                    print(Fore.YELLOW + "This line doesn't exist! You have wasted your move!")

                print(Fore.CYAN + ' '.join(first_row))
                print(Fore.CYAN + ' '.join(second_row))
                print(Fore.CYAN + ' '.join(third_row))

                if first_row[0] == "✘" and first_row[1] == "✘" and first_row[2] == "✘" or second_row[0] == "✘" and second_row[
                    1] == "✘" and second_row[2] == "✘" or third_row[0] == "✘" and third_row[1] == "✘" and third_row[2] == "✘" or \
                        first_row[0] == "✘" and second_row[1] == "✘" and third_row[2] == "✘" or first_row[2] == "✘" and \
                        second_row[1] == "✘" and third_row[0] == "✘" or first_row[0] == "✘" and second_row[0] == "✘" and \
                        third_row[0] == "✘" or first_row[1] == "✘" and second_row[1] == "✘" and third_row[1] == "✘" or \
                        first_row[2] == "✘" and second_row[2] == "✘" and third_row[2] == "✘":
                    first_player_won = "First player won!"
                    time.sleep(1)
                    print_1 = ""
                    for i in range(0, len(first_player_won)):
                        time.sleep(0.1)
                        print_1 += first_player_won[i]
                        print(Fore.RED + print_1)
                    time.sleep(0.2)
                    print(game_over)
                    the_game_is_running = False
                elif first_row.count("□") == 0 and second_row.count("□") == 0 and third_row.count("□") == 0 and the_game_is_running:
                    print(Fore.YELLOW + "Draw!")
                    time.sleep(0.2)
                    print(game_over)
                    the_game_is_running = False

        else:
            current_symbol = second_person_symbol
            time.sleep(0.2)
            selected_line = int(input(Fore.GREEN + "\nPlayer 2, choose a line:  "))
            time.sleep(0.2)
            selected_position = int(input(Fore.GREEN + "Player 2, choose a position: "))
            time.sleep(0.2)
            if selected_position > 3:
                print(Fore.YELLOW + "You have entered an invalid position and wasted your move!")
            else:
                if selected_line == 1:
                    if first_row[selected_position - 1] == "□":
                        first_row.insert((selected_position-1), current_symbol)
                        first_row.pop(selected_position)
                    else:
                        print(Fore.YELLOW + "This position is already taken! You have wasted your move!")

                elif selected_line == 2:
                    if second_row[selected_position - 1] == "□":
                        second_row.insert((selected_position-1), current_symbol)
                        second_row.pop(selected_position)
                    else:
                        print(Fore.YELLOW + "This position is already taken! You have wasted your move!")

                elif selected_line == 3:
                    if third_row[selected_position - 1] == "□":
                        third_row.insert((selected_position-1), current_symbol)
                        third_row.pop(selected_position)
                    else:
                        print(Fore.YELLOW + "This position is already taken! You have wasted your move!")

                else:
                    print(Fore.YELLOW + "This line doesn't exist! You have wasted your move!")

                print(Fore.LIGHTBLUE_EX + ' '.join(first_row))
                print(Fore.LIGHTBLUE_EX + ' '.join(second_row))
                print(Fore.LIGHTBLUE_EX + ' '.join(third_row))

            if first_row[0] == "⬤" and first_row[1] == "⬤" and first_row[2] == "⬤" or second_row[0] == "⬤" and second_row[
                1] == "⬤" and second_row[2] == "⬤" or third_row[0] == "⬤" and third_row[1] == "⬤" and third_row[2] == "⬤" or \
                    first_row[0] == "⬤" and second_row[1] == "⬤" and third_row[2] == "⬤" or first_row[2] == "⬤" and \
                    second_row[1] == "⬤" and third_row[0] == "⬤" or first_row[0] == "⬤" and second_row[0] == "⬤" and \
                    third_row[0] == "⬤" or first_row[1] == "⬤" and second_row[1] == "⬤" and third_row[1] == "⬤" or \
                    first_row[2] == "⬤" and second_row[2] == "⬤" and third_row[2] == "⬤":
                second_player_won = "Second player won!"
                time.sleep(1)
                print_2 = ""
                for i in range(0, len(second_player_won)):
                    time.sleep(0.1)
                    print_2 += second_player_won[i]
                    print(Fore.GREEN + print_2)
                time.sleep(0.2)
                print(game_over)
                the_game_is_running = False
            elif first_row.count("□") == 0 and second_row.count("□") == 0 and third_row.count("□") == 0 and the_game_is_running:
                print(Fore.YELLOW + "Draw!")
                the_game_is_running = False
    time.sleep(3)
    continuation = str(input("Do you wish to play another game? "))

    if continuation == "no":
        print(Fore.CYAN + "Thanks for playing!")
        time.sleep(0.5)
        print(Fore.CYAN + "Bye!")
        the_players_want_to_play = False
    elif continuation == "yes":
        the_players_want_to_play = True
