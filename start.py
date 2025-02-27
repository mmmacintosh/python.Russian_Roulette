import random
import time
import tkinter as tk
from PIL import Image, ImageTk

# Глобальная переменная для подсчёта серии побед
streak = 0


# Функция для очистки экрана (текстового виджета и кнопок)
def clear_screen():
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)
    text_widget.config(state=tk.DISABLED)
    for widget in button_frame.winfo_children():
        widget.destroy()


# Функция для добавления текста по центру с опциональной задержкой
def append_text(text, delay=0):
    text_widget.config(state=tk.NORMAL)
    text_widget.insert(tk.END, text + "\n", "center")
    text_widget.see(tk.END)
    text_widget.config(state=tk.DISABLED)
    if delay:
        root.update()
        time.sleep(delay)


# Функция приветствия (вывод текста слева направо)
def show_welcome():
    clear_screen()
    text_widget.config(fg="orange")
    welcome_txt = "WELCOME TO RUSSIAN ROULLETE"
    text_widget.config(state=tk.NORMAL)
    # Выводим весь текст на одной строке с постепенным добавлением символов
    for char in welcome_txt:
        text_widget.insert(tk.END, char)
        text_widget.see(tk.END)
        text_widget.update()
        time.sleep(0.1)
    text_widget.insert(tk.END, "\n")
    text_widget.config(state=tk.DISABLED)

    # Вывод ASCII-арта заголовка
    ascii_art = [
        "⠀⠀⠀⠀⠀⠀⢦⣤⣴⣶⣶⣶⣶⣶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⣆",
        "⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠏⠉⠉⠉⠉⠉⠉⠉⠉         made by mmmacintosh",
        "⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀",
        "⠀⠀⢀⣾⣿⣿⣿⣿⣿⢿⣿⠛⠿⡿⠛⠃⠀⠀",
        "⠀⢀⣾⣿⣿⠁⠀⠈⠇⠀⢿⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⣾⣿⣿⡇⠀⠀⠀⠈⠂⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⢾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
    ]
    for line in ascii_art:
        append_text(line, delay=0.1)
    root.after(500, show_main_menu)


# Главное меню с информацией о серии и кнопками
def show_main_menu():
    clear_screen()
    append_text(f"Your current streak: {streak}")
    btn_start = tk.Button(button_frame, text="Start Game", font=("Courier", 14),
                          command=start_game, bg="sandybrown", fg="black")
    btn_start.pack(side=tk.LEFT, padx=20, pady=10)
    btn_exit = tk.Button(button_frame, text="Exit", font=("Courier", 14),
                         command=exit_game, bg="sandybrown", fg="black")
    btn_exit.pack(side=tk.LEFT, padx=20, pady=10)


# Запуск игры: вывод сообщения и кнопки "Shot"
def start_game():
    clear_screen()
    append_text('Game Started, press the "Shot" button to shoot yourself')
    btn_shot = tk.Button(button_frame, text="Shot", font=("Courier", 14),
                         command=do_shot, bg="sandybrown", fg="black")
    btn_shot.pack(padx=20, pady=10)


# Логика выстрела
def do_shot():
    global streak
    clear_screen()
    DeathBullet = random.randint(1, 6)
    DeathRoulette1 = random.randint(1, 6)
    if DeathBullet == DeathRoulette1:
        death_lines = [
            "", "YOU DIED",
            "     .... NO! ...                  ... MNO! ...",
            "   ..... MNO!! ...................... MNNOO! ...",
            " ..... MMNO! ......................... MNNOO!! .",
            ".... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .",
            " ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....",
            "    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...",
            "   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....",
            "   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  ",
            "    ....... MMMMM..    OPPMMP    .,OMI! ....",
            "     ...... MMMM::   o.,OPMP,.o   ::I!! ...",
            "         .... NNM:::.,,OOPM!P,.::::!! ....",
            "          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....",
            "         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....",
            "           .. MMMMMNNOOMMNNIIIPPPOO!! ......",
            "          ...... MMMONNMMNNNIIIOO!..........",
            "       ....... MN MOMMMNNNIIIIIO! OO ..........",
            "    ......... MNO! IiiiiiiiiiiiI OOOO ...........",
            "    ......... MNO! IiiiiiiiiiiiI OOOO ...........",
            "  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........",
            "   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........",
            "   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........",
            "      ...... OO! ................. ON! .......",
            "         ................................"
        ]
        delay = 100
        total_delay = 0
        for line in death_lines:
            root.after(total_delay, lambda l=line: append_text(l))
            total_delay += delay
        root.after(total_delay + 500, lambda: append_text(f"Your Streak was: {streak}"))
        root.after(total_delay + 1000, show_restart_menu)
    else:
        append_text("You WIN")
        streak += 1
        win_art = [
            "⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⣦⠀⠀",
            "⠀⠀⣠⣤⣤⣄⣀⣾⣿⠟⠛⠻⢿⣷⠀",
            "⢰⣿⡿⠛⠙⠻⣿⣿⠁⠀⠀⠀⣶⢿⡇",
            "⢿⣿⣇⠀⠀⠀⠈⠏⠀⠀⠀ survived",
            "⠀⠻⣿⣷⣦⣤⣀⠀⠀⠀⠀⣾⡿⠃⠀",
            "⠀⠀⠀⠀⠉⠉⠻⣿⣄⣴⣿⠟⠀⠀⠀",
            "⠀⠀⠀⠀⠀⠀⠀⣿⡿⠟⠁⠀⠀⠀⠀"
        ]
        for line in win_art:
            append_text(line, delay=0.1)
        append_text(f"\nYour Streak: {streak}")
        root.after(1500, show_main_menu)


# Меню перезапуска после смерти
def show_restart_menu():
    clear_screen()
    append_text(f"Your Streak was: {streak}")
    btn_restart = tk.Button(button_frame, text="Restart Game", font=("Courier", 14),
                            command=show_main_menu, bg="sandybrown", fg="black")
    btn_restart.pack(side=tk.LEFT, padx=20, pady=10)
    btn_exit = tk.Button(button_frame, text="Exit", font=("Courier", 14),
                         command=exit_game, bg="sandybrown", fg="black")
    btn_exit.pack(side=tk.LEFT, padx=20, pady=10)


# Завершение игры с сообщением и ASCII-артом пистолета
def exit_game():
    clear_screen()
    text_widget.config(fg="orange")
    append_text("Thanks for playing", delay=0)
    exit_art = [
        "          _,--'\"-.",
        "        ,'        `.",
        "       /            \\\\",
        "      |              |",
        "      |,  .-.  .-.  ,|",
        "      | )(__/  \\__)( |",
        "      |/     /\\     \\|",
        "      (_     ^^     _)",
        "       \\__|IIIIII|__/",
        "        | \\IIIIII/ |",
        "        \\          /",
        "         `--------`"
    ]
    for line in exit_art:
        append_text(line, delay=0.1)
    text_widget.config(fg="orange")
    append_text("\nGame exits in 3 seconds")
    root.after(3000, root.destroy)


# Инициализация главного окна Tkinter
root = tk.Tk()
root.title("Russian Roulette")
root.geometry("800x600")
root.resizable(False, False)

# Загрузка фонового изображения (дикого запада)
try:
    bg_image = Image.open("wildwest.jpg")
except Exception as e:
    print("Background image 'wildwest.jpg' not found. Make sure it exists in the working directory.")
    exit(1)
bg_image = bg_image.resize((800, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Размещение фонового изображения
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создаем текстовый виджет с прозрачным фоном (без переноса строк)
text_widget = tk.Text(root, bg="lightyellow", fg="orange", font=("Courier", 14), bd=0, highlightthickness=0,
                      wrap="none")
text_widget.place(relx=0.5, rely=0.5, anchor="center", width=750, height=400)
text_widget.tag_configure("center", justify="center")

# Фрейм для кнопок (располагаем внизу окна)
button_frame = tk.Frame(root, bg="lightyellow")
button_frame.place(relx=0.5, rely=0.9, anchor="center")

# Запуск приветствия
show_welcome()
root.mainloop()
