import random

wins_count = []
big_database = []
interests = []
choice = None

print("\033[34mWelcome!")

while True:
    print("\033[34mMenu: ->")
    print("\033[34mSave my personal information: ->(1)<-")
    print("\033[34mView and delete personal information: ->(2)<-")
    print("\033[34mEnter the calculator: ->(3)<-")
    print("\033[34mPlay a game (Tic-Tac-Toe): ->(4)<-")
    choice = int(input())

    if choice == 1:
        name = None
        s = 0
        t = []

        while not name:
            name = input("\033[32mEnter your name, only letters are allowed!: ")
            if len(name) > 1:
                w = 0
                for i in range(len(name)):
                    if name[i] in "qwertyuiopasdfghjklzxcvbnm'QWERTYUIOPASDFGHJKLZXCVBNM":
                        w += 1
                if len(name) == w:
                    t.append(name.title())
                    break
                else:
                    print("\033[31mNames must only contain letters!")
                    name = None

        surname = None
        while not surname:
            surname = input("\033[32mEnter your surname, only letters are allowed!: ")
            if len(surname) > 1:
                w = 0
                for i in range(len(surname)):
                    if surname[i] in "qwertyuiopasdfghjklzxcvbnm'QWERTYUIOPASDFGHJKLZXCVBNM":
                        w += 1
                if len(surname) == w:
                    t.append(surname.title())
                    break
                else:
                    print("\033[31mSurnames must only contain letters!")
                    surname = None

        age = None
        while not age:
            age = input("\033[32mEnter your age, it must be a number and between 6 and 100!: ")
            if age.isdigit() and 6 <= int(age) <= 100:
                t.append(age)
                break
            else:
                print("\033[31mYour age must be a number and between 6 and 100!")

        interest1 = None
        interest2 = []
        while not interest1:
            print("Enter your interests: ->")
            print("If none, type 'no': ->")
            interest1 = str(input()).lower()
            if len(interest1) == 0 or interest1 == "no":
                interest2.append("No interests!")
                interest1 = None
                break
            else:
                interest2.append(str(interest1))
                interest1 = None
                break
        
        interests.append(interest2)
        big_database.append(t)
        print("\033[31mData saved!")
        t = []
        interest = []

    elif choice == 2:
        if len(big_database) == 0:
            print("\033[33mSorry, no data available: :'(")
        else:
            print(f"You have {len(big_database)} data records:")
            print("Do you want to see them? (yes or no)")
            yes_no = input().lower()

            if yes_no == "yes":
                s = 0
                for item in big_database:
                    s += 1
                    print(f"{s}. Name: {item[0]}, Surname: {item[1]}, Age: {item[2]}")
                    print(f"Their interests: -> {interests[s-1]}")
                print("Do you want to delete any records? (yes or no)")
                yes_no1 = input().lower()

                if yes_no1 == "yes":
                    print("Enter the number of the record to delete")
                    delete = int(input()) - 1
                    if 0 <= delete < len(big_database):
                        big_database.pop(delete)
                        print("\033[31mData deleted!")
                    else:
                        print("\033[31mError: No such record exists!")
            elif yes_no == "no":
                choice = None

    elif choice == 3:
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            if y != 0:
                return x / y
            else:
                return "Cannot divide by 0"

        while True:
            print("\nCalculator")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            choice1 = input("Enter your choice (1/2/3/4/5): ")
            if choice1 == '5':
                choice = None
                break
            if choice1 in ['1', '2', '3', '4']:
                try:
                    x = float(input("Enter the first number: "))
                    y = float(input("Enter the second number: "))
                except ValueError:
                    print("Please enter a valid number!")
                    continue
                if choice1 == '1':
                    print(f"{x} + {y} = {add(x, y)}")
                elif choice1 == '2':
                    print(f"{x} - {y} = {subtract(x, y)}")
                elif choice1 == '3':
                    print(f"{x} * {y} = {multiply(x, y)}")
                elif choice1 == '4':
                    print(f"{x} / {y} = {divide(x, y)}")
            else:
                print("Please enter a valid choice!")

    elif choice == 4:
        print("Welcome!")
        print("Do you want to play with a bot or without one? (without bot or with bot)")
        bot = None
        while not bot:
            bot = str(input())
            if bot == "without bot":
                def print_board(board):
                    for i in range(3):
                        print(" | ".join(board[i]))
                        if i < 2:
                            print("---------")

                def player_move(board, player):
                    while True:
                        try:
                            move = int(input(f"\033[31mPlayer {player}, enter a position on the board (1-9): ")) - 1
                            row, col = divmod(move, 3)
                            if board[row][col] == " ":
                                board[row][col] = player
                                break
                            else:
                                print("\033[31mThis spot is taken, choose another spot!")
                        except (ValueError, IndexError):
                            print("\033[31mInvalid input! Please enter a number between 1 and 9.")

                def check_winner(board, player):
                    for i in range(3):
                        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
                            return True
                        if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
                            return True
                    return False

                def tic_tac_toe():
                    board = [[" " for _ in range(3)] for _ in range(3)]
                    players = ["X", "O"]
                    turn = 0
                    print("\033[31mX and O game started!\n")
                    print_board(board)
                    while True:
                        current_player = players[turn % 2]
                        player_move(board, current_player)
                        print_board(board)
                        if check_winner(board, current_player):
                            print(f"\033[31mPlayer {current_player} won!")
                            break
                        if all(board[i][j] != " " for i in range(3) for j in range(3)):
                            print("\033[31mThe game is a draw!")
                            break
                        turn += 1

                if __name__ == "__main__":
                    tic_tac_toe()

            elif bot == "with bot":
                import random
                def print_board(board):
                    for i in range(3):
                        print(" | ".join(board[i]))
                        if i < 2:
                            print("---------")

                def player_move(board, player):
                    while True:
                        try:
                            move = int(input(f"\033[31mPlayer {player}, enter a position on the board (1-9): ")) - 1
                            row, col = divmod(move, 3)
                            if board[row][col] == " ":
                                board[row][col] = player
                                break
                            else:
                                print("\033[31mThis spot is taken, choose another spot!")
                        except (ValueError, IndexError):
                            print("\033[31mInvalid input! Please enter a number between 1 and 9.")

                def bot_move(board, player):
                    while True:
                        move = random.randint(0, 8)
                        row, col = divmod(move, 3)
                        if board[row][col] == " ":
                            board[row][col] = player
                            print(f"\033[31mBot {player} is making a move...")
                            break

                def check_winner(board, player):
                    for i in range(3):
                        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
                            return True
                        if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
                            return True
                    return False

                def tic_tac_toe():
                    board = [[" " for _ in range(3)] for _ in range(3)]
                    players = ["X", "O"]
                    turn = 0
                    print("\033[31mX and O game started!\n")
                    print_board(board)
                    while True:
                        if turn % 2 == 0:
                            current_player = players[turn % 2]
                            player_move(board, current_player)
                        else:
                            current_player = players[turn % 2]
                            bot_move(board, current_player)
                        print_board(board)
                        if check_winner(board, current_player):
                            if turn % 2 == 0:
                                print(f"\033[31mPlayer {current_player} won!")
                            else:
                                print(f"\033[31mBot {current_player} won!")
                            break
                        if all(board[i][j] != " " for i in range(3) for j in range(3)):
                            print("\033[31mThe game is a draw!")
                            break
                        turn += 1

                if __name__ == "__main__":
                    tic_tac_toe()
