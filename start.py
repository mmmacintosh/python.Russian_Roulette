#импорты
import random
import time
import sys

# оформление 
print("\033[31m", end='')

txt = 'WELCOME TO RUSSIAN ROULLETE'
for char in txt:
    time.sleep(0.2)
    print(char, end='', flush=True)

print("\n\n")
time.sleep(0.3)
print('⠀⠀⠀⠀⠀⠀⢦⣤⣴⣶⣶⣶⣶⣶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⣆')
time.sleep(0.2)
print('⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠏⠉⠉⠉⠉⠉⠉⠉⠉         S̴Y̴S̴T̴E̴M̴3̴2̴')
time.sleep(0.2)
print('⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀')
time.sleep(0.2)
print('⠀⠀⢀⣾⣿⣿⣿⣿⣿⢿⣿⠛⠿⡿⠛⠃⠀⠀')
time.sleep(0.2)
print('⠀⢀⣾⣿⣿⠁⠀⠈⠇⠀⢿⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
time.sleep(0.2)
print('⠀⣾⣿⣿⡇⠀⠀⠀⠈⠂⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
time.sleep(0.2)
print('⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
time.sleep(0.2)
print('⢾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
print("\n\n")
time.sleep(0.3)

streak = 0
# игровой цикл
while True:
    print('Start Game - 1')
    print('Exit - 0')
    game_choice = int(input('Input: '))
    if game_choice == 1:
        print('Game Started, type "shot" to shot yourself')
        shot = input('Answer: ')
        if shot == 'shot':
            # Для эмуляции шансов используем случайное число от 1 до 6
            DeathBullet = random.randint(1, 6)
            DeathRoulette1 = random.randint(1, 6)
            if DeathBullet == DeathRoulette1:
                print("\n\n\n")
                print('YOU DIED')
                print("\n\n\n")
                time.sleep(0.1)
                print('     .... NO! ...                  ... MNO! ...')
                time.sleep(0.1)
                print('   ..... MNO!! ...................... MNNOO! ...')
                time.sleep(0.1)
                print(' ..... MMNO! ......................... MNNOO!! .')
                time.sleep(0.1)
                print('.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .')
                time.sleep(0.1)
                print(' ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....')
                time.sleep(0.1)
                print('    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...')
                time.sleep(0.1)
                print('   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....')
                time.sleep(0.1)
                print('   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  ')
                time.sleep(0.1)
                print('    ....... MMMMM..    OPPMMP    .,OMI! ....')
                time.sleep(0.1)
                print('     ...... MMMM::   o.,OPMP,.o   ::I!! ...')
                time.sleep(0.1)
                print('         .... NNM:::.,,OOPM!P,.::::!! ....')
                time.sleep(0.1)
                print('          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....')
                time.sleep(0.1)
                print('         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....')
                time.sleep(0.1)
                print('           .. MMMMMNNOOMMNNIIIPPPOO!! ......')
                time.sleep(0.1)
                print('          ...... MMMONNMMNNNIIIOO!..........')
                time.sleep(0.1)
                print('       ....... MN MOMMMNNNIIIIIO! OO ..........')
                time.sleep(0.1)
                print('    ......... MNO! IiiiiiiiiiiiI OOOO ...........')
                time.sleep(0.1)
                print('    ......... MNO! IiiiiiiiiiiiI OOOO ...........')
                time.sleep(0.1)
                print('  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........')
                time.sleep(0.1)
                print('   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........')
                time.sleep(0.1)
                print('   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........')
                time.sleep(0.1)
                print('      ...... OO! ................. ON! .......')
                time.sleep(0.1)
                print('         ................................')
                print("\n\n")
                print('Your Streak was: ' + str(streak))
                break
            else:
                print("\n\n\n")
                print('You WIN')
                print("\n\n\n")
                streak += 1
        else:
            print("Invalid input. Try again.")
    elif game_choice == 0:
        sys.exit()
    else:
        print("Invalid input. Try again.")

    # второй блок ASCII-арта
    print("#                            ,.--------._                                            #")
    time.sleep(0.1)
    print("#                           /            ''.                                         #")
    time.sleep(0.1)
    print("#                         ,'                \\     |\"                /\\          /\\  #")
    time.sleep(0.1)
    print("#                /\"|     /                   \\    |\"              ( \\        // ) #")
    time.sleep(0.1)
    print("#               \"_\"|    /           z#####z   \\  //                  \\ \\      // /  #")
    time.sleep(0.1)
    print("#                 \\  #####        ##------\".  \\//                    \\_\\||||//_/   #")
    time.sleep(0.1)
    print("#                  \\/-----\\     /          \".  \\                      \\/ _  _ \\     #")
    time.sleep(0.1)
    print("#                   \\|      \\   |   ,,--..       \\                    \\/|(O)(O)|     #")
    time.sleep(0.1)
    print("#                   | ,.--._ \\  (  | ##   \\)      \\                  \\/ |      |     #")
    time.sleep(0.1)
    print("#                   |(  ##  )/   \\ `-....-//       |///////////////_\\/  \\      /     #")
    time.sleep(0.1)
    print("#                     '--'.\"      \\                \\              //     |____|      #")
    time.sleep(0.1)
    print("#                  /'    /         ) --.            \\            ||     /      \\     #")
    time.sleep(0.1)
    print("#               ,..|     \\.________/    `-..         \\   \\       \\|     \\ 0  0 /     #")
    time.sleep(0.1)
    print("#            _,##/ |   ,/   /   \\           \\         \\   \\       U    / \\_//_/      #")
    time.sleep(0.1)
    print("#          :###.-  |  ,/   /     \\        /' \"\"      .\\        (     /              #")
    time.sleep(0.1)
    print("#         /####|   |   (.___________,---',/    |       |\\=._____|  |_/               #")
    time.sleep(0.1)
    print("#        /#####|   |     \\|||__|_,/             |####\\    |                  #")
    time.sleep(0.1)
    print("#       /######\\   \\      \\__________/                /#####|   \\                  #")
    time.sleep(0.1)
    print("#      /|#######`. `\\                                /#######\\   |                 #")
    time.sleep(0.1)
    print("#     /++\\#########\\  \\                      _,'    _/#########\\ |                 #")
    time.sleep(0.1)
    print("#    /++++|#########|  \\      .---..       ,/      ,'##########.\\|_||  Donkey By     #")
    time.sleep(0.1)
    print("#   //++++|#########\\.  \\.              ,-/      ,'########,+++++\\_\\ Hard'96       #")
    time.sleep(0.1)
    print("#  /++++++|##########\\.   '._        _,/       ,'######,''++++++++\\                  #")
    time.sleep(0.1)
    print("# |+++++++|###########|       -----.\"        _'#######' +++++++++++\\                 #")
    time.sleep(0.1)
    print("# |+++++++|############\\.     \\     //      /#######/++++ S@yaN +++\\                #")
    time.sleep(0.1)
    print("#      ____________________\\___//__________________________________         #")
    time.sleep(0.1)
    print()
    print()
    print()
    print('Your Streak: ' + str(streak))
