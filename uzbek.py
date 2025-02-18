import random

oyinda_yutgan_soni = []
katta_malumot_bazasi = []
qiziqishlar = []
tanlash = None

print("\033[34mHush kelibsiz!")

while True:
    print("\033[34mmenyu: ->")
    print("\033[34mo'zim haqimda ma'lumot saqlash: ->(1)<-")
    print("\033[34mo'zim haqimda ma'lumotlarni ko'rish va o'chirish: ->(2)<-")
    print("\033[34mkalkulyatorga kirish: ->(3)<-")
    print("\033[34mo'yin oynash (x va 0 o'yini): ->(4)<-")
    tanlash = int(input())

    if tanlash == 1:
        name = None
        s = 0
        t = []

        while not name:
            name = input("\033[32mIsmingizni kiriting faqat harflar mumkun!: ")
            if len(name) > 1:
                w = 0
                for i in range(len(name)):
                    if name[i] in "qwertyuiopasdfghjklzxcvbnm'QWERTYUIOPASDFGHJKLZXCVBNM":
                        w += 1
                if len(name) == w:
                    t.append(name.title())
                    break
                else:
                    print("\033[31mIsmlar faqat harflardan iborat bo'lishi kerak!")
                    name = None

        familiya = None
        while not familiya:
            familiya = input("\033[32mfamiliyangizni kiriting faqat harflar mumkun!: ")
            if len(familiya) > 1:
                w = 0
                for i in range(len(familiya)):
                    if familiya[i] in "qwertyuiopasdfghjklzxcvbnm'QWERTYUIOPASDFGHJKLZXCVBNM":
                        w += 1
                if len(familiya) == w:
                    t.append(familiya.title())
                    break
                else:
                    print("\033[31mfamiliyada faqat harflardan iborat bo'lishi kerak!")
                    familiya = None

        yosh = None
        while not yosh:
            yosh = input("\033[32myoshingizni kiriting faqat raqamlardan iborat bo'lishi kerak va 6 dan 80 yosh oralig'ida bo'lishi kerak!: ")
            if yosh.isdigit() and 6 <= int(yosh) <= 100:
                t.append(yosh)
                break
            else:
                print("\033[31myoshingiz faqat raqamlardan iborat bo'lishi kerak va 6 dan 80 yosh oralig'ida bo'lishi kerak!")
        
        qiziqish1 = None
        qiziqish2 = []
        while not qiziqish1:
            print("qiziqishlaringizni yozib qoying: ->")
            print("agar bo'lmasa yoq deb yozing: ->")
            qiziqish1 = str(input()).lower()
            if len(qiziqish1) == 0 or qiziqish1 == "yoq":
                qiziqish2.append("qiziqish yoq!")
                qiziqish1 = None
                break
            else:
                qiziqish2.append(str(qiziqish1))
                qiziqish1 = None
                break
        
        qiziqishlar.append(qiziqish2)
        katta_malumot_bazasi.append(t)
        print("\033[31mmalumotlar saqlandi!")
        t = []
        qiziqish = []

    elif tanlash == 2:
        if len(katta_malumot_bazasi) == 0:
            print("\033[33mafsus malumotlar mavjud emas: :'(")
        else:
            print(f"sizda {len(katta_malumot_bazasi)} ta malumotlar mavjud:")
            print("siz ularni kormoqchimisiz? (ha yoki yoq)")
            ha_yoq = input().lower()

            if ha_yoq == "ha":
                s = 0
                for item in katta_malumot_bazasi:
                    s += 1
                    print(f"{s}.ismi: {item[0]}, familiyasi: {item[1]}, yoshi: {item[2]}")
                    print(f"uning qiziqishlari: -> {qiziqishlar[s-1]}")
                print("ularni ochirmoqchimisiz? (ha yoki yoq)")
                ha_yoq1 = input().lower()

                if ha_yoq1 == "ha":
                    print("ochirmoqchi bo'lgan ma'lumot sonini kiriting")
                    ochirish = int(input()) - 1
                    if 0 <= ochirish < len(katta_malumot_bazasi):
                        katta_malumot_bazasi.pop(ochirish)
                        print("\033[31mmalumot o'chirildi!")
                    else:
                        print("\033[31mXato: Bunday ma'lumot mavjud emas!")
            elif ha_yoq == "yoq":
                tanlash = None

    elif tanlash == 3:
        def qoshish(x, y):
            return x + y
        def ayirish(x, y):
            return x - y
        def kopaytirish(x, y):
            return x * y
        def bolish(x, y):
            if y != 0:
                return x / y
            else:
                return "0 ga bolinmaydi"

        while True:
            print("\nKalkulyator")
            print("1. Qoshish")
            print("2. Ayirish")
            print("3. Kopaytirish")
            print("4. Bolish")
            print("5. Chiqish")
            tanlov1 = input("Tanlovni kiriting (1/2/3/4/5): ")
            if tanlov1 == '5':
                tanlash = None
                break
            if tanlov1 in ['1', '2', '3', '4']:
                try:
                    x = float(input("Birinchi sonni kiriting: "))
                    y = float(input("Ikkinchi sonni kiriting: "))
                except ValueError:
                    print("Iltimos, sonni to'g'ri kiriting!")
                    continue
                if tanlov1 == '1':
                    print(f"{x} + {y} = {qoshish(x, y)}")
                elif tanlov1 == '2':
                    print(f"{x} - {y} = {ayirish(x, y)}")
                elif tanlov1 == '3':
                    print(f"{x} * {y} = {kopaytirish(x, y)}")
                elif tanlov1 == '4':
                    print(f"{x} / {y} = {bolish(x, y)}")
            else:
                print("Iltimos, to'g'ri tanlov kiriting!")

    elif tanlash == 4:
        print("hush kelibsiz !")
        print("bot bilanmi yoki botsiz? (botsiz yoki botli)")
        bot = None
        while not bot:
            bot = str(input())
            if bot == "botsiz":
                def print_board(board):
                    for i in range(3):
                        print(" | ".join(board[i]))
                        if i < 2:
                            print("---------")

                def player_move(board, player):
                    while True:
                        try:
                            move = int(input(f"\033[31mO'yinchi {player}, taxtada joyni kiriting (1-9): ")) - 1
                            row, col = divmod(move, 3)
                            if board[row][col] == " ":
                                board[row][col] = player
                                break
                            else:
                                print("\033[31mBu joy band, boshqa joyni tanlang!")
                        except (ValueError, IndexError):
                            print("\033[31mNoto'g'ri kiritish! Iltimos, 1 dan 9 gacha bo'lgan sonni kiriting.")

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
                    print("\033[31mX va 0 o'yini boshlandi!\n")
                    print_board(board)
                    while True:
                        current_player = players[turn % 2]
                        player_move(board, current_player)
                        print_board(board)
                        if check_winner(board, current_player):
                            print(f"\033[31mO'yinchi {current_player} g'olib bo'ldi!")
                            break
                        if all(board[i][j] != " " for i in range(3) for j in range(3)):
                            print("\033[31mO'yin durang bo'ldi!")
                            break
                        turn += 1

                if __name__ == "__main__":
                    tic_tac_toe()

            elif bot == "botli":
                import random
                def print_board(board):
                    for i in range(3):
                        print(" | ".join(board[i]))
                        if i < 2:
                            print("---------")

                def player_move(board, player):
                    while True:
                        try:
                            move = int(input(f"\033[31mO'yinchi {player}, taxtada joyni kiriting (1-9): ")) - 1
                            row, col = divmod(move, 3)
                            if board[row][col] == " ":
                                board[row][col] = player
                                break
                            else:
                                print("\033[31mBu joy band, boshqa joyni tanlang!")
                        except (ValueError, IndexError):
                            print("\033[31mNoto'g'ri kiritish! Iltimos, 1 dan 9 gacha bo'lgan sonni kiriting.")

                def bot_move(board, player):
                    while True:
                        move = random.randint(0, 8)
                        row, col = divmod(move, 3)
                        if board[row][col] == " ":
                            board[row][col] = player
                            print(f"\033[31mBot {player} harakat qilmoqda...")
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
                    print("\033[31mX va 0 o'yini boshlandi!\n")
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
                                print(f"\033[31mO'yinchi {current_player} g'olib bo'ldi!")
                            else:
                                print(f"\033[31mBot {current_player} g'olib bo'ldi!")
                            break
                        if all(board[i][j] != " " for i in range(3) for j in range(3)):
                            print("\033[31mO'yin durang bo'ldi!")
                            break
                        turn += 1

                if __name__ == "__main__":
                    tic_tac_toe()
