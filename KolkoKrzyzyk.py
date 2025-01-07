import time
def display_board_player(baza):
    return print(f'\n', baza[0],'|', baza[1],'|', baza[2],'|',f'\n','-'*11, f'\n', baza[3],'|', baza[4],'|', baza[5],'|'
                 ,f'\n','-'*11,f'\n', baza[6],'|', baza[7],'|', baza[8],'|',f'\n')
def game_system():
    while True:
        try:
            miejsce = int(input('Wybierz miejsce: '))
            if miejsce in range(1, 10):
                return miejsce
            else:
                print('Wybierz prawidłowe miejsce!')
        except (ValueError):
            print('Wpisz cyfrę!')
            continue
def check_System(baza_game):
    baza = baza_game
    dic = {1:[baza[0],baza[1],baza[2]],2:[baza[3],baza[4],baza[5]],3:[baza[6],baza[7],baza[8]]
           ,4:[baza[0],baza[3],baza[6]],5:[baza[1],baza[4],baza[7]],6:[baza[2],baza[5],baza[8]]
           ,7:[baza[0],baza[4],baza[8]],8:[baza[2],baza[4],baza[6]]}
    lista = []
    check = ['X','X','X']
    check1 = ['#','#','#']
    k = 0
    while k <= 7:
        k += 1
        for i in dic[k]:
            if i == 'X':
                lista.append(i)
                if lista == check:
                    return "1"
            if i == '#':
                lista.append(i)
                if lista == check1:
                    return "2"
        lista.clear()

gracze = ['X', '#', 'X', '#','X', '#', 'X', '#','X']
baza = [7, 8, 9, 4, 5, 6, 1, 2, 3]
while True:
    try:
        print('Wybiera gracz',gracze[0])
        time.sleep(1)
        display_board_player(baza)
        time.sleep(1)
        miejsce = baza.index(game_system())
        baza[miejsce] = gracze[0]
    except(ValueError):
        print('Wybierz inne miejsce!')
        continue
    gracze.pop(0)
    if check_System(baza) == "1":
        display_board_player(baza)
        print('Gracz "X" Wygrywa!')
        break
    elif check_System(baza) == "2":
        display_board_player(baza)
        print('Gracz "#" Wygrywa!')
        break
    elif gracze == []:
        print('Remis!')
        break
















