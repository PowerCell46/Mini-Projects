import random
import pyfiglet
from colorama import Fore
import time

print("\n" + time.asctime() + "\n")

first_person_symbol = '✘'
second_person_symbol = '⬤'
the_players_want_to_play = True

print(Fore.CYAN + pyfiglet.figlet_format("Welcome!", font="big"))
time.sleep(1.5)

print(Fore.CYAN + pyfiglet.figlet_format("Let's play Tic_Tac_Toe!", font="big"))
time.sleep(1.5)


do_you_know_the_rules = str(input(Fore.LIGHTWHITE_EX + "Are you familiar with the game? (Yes/No) "))

if do_you_know_the_rules.lower() == "no":
    print("\n Two players take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.")
    time.sleep(8)
    more_info = str(input("\nDo you need more explanation before starting the game? (Yes/No) "))
    if more_info.lower() == "yes":
        print("\n https://www.youtube.com/watch?v=USEjXNCTvcc")
        time.sleep(15)


while the_players_want_to_play:
    player_vs_player_or_player_vs_bot = str(input("How do you wish to play? Versus a bot or versus another player? (with a bot/with another player) "))

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

        if index % 2 == 0:  # First player's turn
            try:
                current_symbol = first_person_symbol
                time.sleep(0.2)
                selected_line = int(input(Fore.CYAN + "\nPlayer 1, choose a line: "))
                time.sleep(0.2)
                selected_position = int(input(Fore.CYAN + "Player 1, choose a position: "))
                time.sleep(0.2)

                if selected_position > 3 or selected_position < 1:
                    raise IndexError

                else:  # The entered row and column are valid
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
                        raise IndexError

                    print(Fore.CYAN + ' '.join(first_row))
                    print(Fore.CYAN + ' '.join(second_row))
                    print(Fore.CYAN + ' '.join(third_row))

                    if first_row[0] == "✘" and first_row[1] == "✘" and first_row[2] == "✘" or second_row[0] == "✘" and \
                            second_row[
                                1] == "✘" and second_row[2] == "✘" or third_row[0] == "✘" and third_row[1] == "✘" and \
                            third_row[2] == "✘" or \
                            first_row[0] == "✘" and second_row[1] == "✘" and third_row[2] == "✘" or first_row[
                        2] == "✘" and \
                            second_row[1] == "✘" and third_row[0] == "✘" or first_row[0] == "✘" and second_row[
                        0] == "✘" and \
                            third_row[0] == "✘" or first_row[1] == "✘" and second_row[1] == "✘" and third_row[
                        1] == "✘" or \
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

                    elif first_row.count("□") == 0 and second_row.count("□") == 0 and third_row.count(
                            "□") == 0 and the_game_is_running:
                        print(Fore.YELLOW + pyfiglet.figlet_format("Draw!", font="slant"))
                        time.sleep(0.3)
                        print(game_over)
                        the_game_is_running = False

            except:
                print(Fore.YELLOW + "You have entered an invalid position! Try again!")
                index -= 1

        else:  # Second Player's turn
            try:
                current_symbol = second_person_symbol
                time.sleep(0.2)
                if player_vs_player_or_player_vs_bot.lower() != "with a bot":
                    selected_line = int(input(Fore.GREEN + "\nPlayer 2, choose a line: "))
                    time.sleep(0.2)
                    selected_position = int(input(Fore.GREEN + "Player 2, choose a position: "))
                    time.sleep(0.2)

                elif player_vs_player_or_player_vs_bot.lower() == "with a bot":
                    selected_line = random.randint(1, 3)
                    print(Fore.LIGHTWHITE_EX + 'The bot is choosing a position.')
                    time.sleep(0.5)
                    while True:
                        if selected_line == 1:
                            if "□" in first_row:
                                break
                        elif selected_line == 2:
                            if "□" in second_row:
                                break
                        elif selected_line == 3:
                            if "□" in third_row:
                                break
                        selected_line = random.randint(1, 3)
                    time.sleep(0.2)
                    selected_position = random.randint(1, 3)
                while True:
                    if selected_position > 3:
                        raise IndexError

                    else:
                        if selected_line == 1:
                            if first_row[selected_position - 1] == "□":
                                first_row.insert((selected_position-1), current_symbol)
                                first_row.pop(selected_position)
                                break
                            else:
                                if player_vs_player_or_player_vs_bot == "with a bot":
                                    selected_position = random.randint(1, 3)
                                else:
                                    print(Fore.YELLOW + "This position is already taken! You have wasted your move!")
                                    break

                        elif selected_line == 2:
                            if second_row[selected_position - 1] == "□":
                                second_row.insert((selected_position-1), current_symbol)
                                second_row.pop(selected_position)
                                break
                            else:
                                if player_vs_player_or_player_vs_bot == "with a bot":
                                    selected_position = random.randint(1, 3)
                                else:
                                    print(Fore.YELLOW + "This position is already taken! You have wasted your move!")
                                    break

                        elif selected_line == 3:
                            if third_row[selected_position - 1] == "□":
                                third_row.insert((selected_position-1), current_symbol)
                                third_row.pop(selected_position)
                                break
                            else:
                                if player_vs_player_or_player_vs_bot == "with a bot":
                                    selected_position = random.randint(1, 3)
                                else:
                                    print(Fore.YELLOW + "This position is already taken! You have wasted your move!")
                                    break

                        else:
                            raise IndexError

                if player_vs_player_or_player_vs_bot == "with a bot":
                    print(Fore.LIGHTWHITE_EX + ' '.join(first_row))
                    print(Fore.LIGHTWHITE_EX + ' '.join(second_row))
                    print(Fore.LIGHTWHITE_EX + ' '.join(third_row))

                else:
                    print(Fore.GREEN + ' '.join(first_row))
                    print(Fore.GREEN + ' '.join(second_row))
                    print(Fore.GREEN + ' '.join(third_row))

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
                    print(Fore.YELLOW + pyfiglet.figlet_format("Draw!", font="slant"))
                    time.sleep(0.3)
                    the_game_is_running = False

            except:
                print(Fore.YELLOW + "You have entered an invalid position! Try again!")
                index -= 1


    time.sleep(3)
    continuation = str(input("Do you wish to play another game? (Yes/No) "))

    if continuation.lower() != "yes":
        print(Fore.CYAN + "Thanks for playing!")
        time.sleep(0.5)
        print(Fore.CYAN + "Bye!")
        the_players_want_to_play = False
    elif continuation.lower() == "yes":
        the_players_want_to_play = True
