import random
import time
import tkinter as tk
from PIL import Image, ImageTk
import sys
import os


# Функция для получения пути к ресурсу (работает для PyInstaller и разработки)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Функции для работы с файлом highscore.txt
HIGH_SCORE_FILE = "highscore.txt"


def load_highscore():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r") as f:
                return int(f.read())
        except Exception:
            return 0
    else:
        return 0


def save_highscore(score):
    try:
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(score))
    except Exception:
        pass


# Глобальные переменные
streak = 0
highscore = load_highscore()


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


# Функция, выводящая описание бара вечером
def show_description():
    clear_screen()
    text_widget.config(fg="orange")
    description = [
        "In the dim glow of neon lights, you find yourself in an old, rustic bar.",
        "The evening air is thick with mystery and the scent of aged whiskey.",
        "Flickering candles and worn wooden tables set the stage for an unforgettable night.",
        "A sense of danger and excitement lingers in every shadow...",
    ]
    for line in description:
        append_text(line, delay=0.2)
    # После описания выводим кнопку Enter bar через 1 секунду
    root.after(1000, show_initial_menu)


# Начальное меню с кнопкой "Enter bar"
def show_initial_menu():
    # Здесь не очищаем экран повторно, чтобы описание осталось видимым
    btn_enter = tk.Button(button_frame, text="Enter bar", font=("Courier", 14),
                          command=show_welcome, bg="sandybrown", fg="black")
    btn_enter.pack(side=tk.LEFT, padx=20, pady=10)


# Приветствие: вывод текста слева направо
def show_welcome():
    clear_screen()
    text_widget.config(fg="orange")
    welcome_txt = "'WELCOME TO RUSSIAN ROULLETE' - said the cowboy on the far table..."
    text_widget.config(state=tk.NORMAL)
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
        "⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠏⠉⠉⠉⠉⠉⠉⠉⠉",
        "⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀            ",
        "⠀⠀⢀⣾⣿⣿⣿⣿⣿⢿⣿⠛⠿⡿⠛⠃⠀⠀          ",
        "⠀⢀⣾⣿⣿⠁⠀⠈⠇⠀⢿⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⣾⣿⣿⡇⠀⠀⠀⠈⠂⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⢾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "                               ",
        "made by mmmacintosh"
    ]
    for line in ascii_art:
        append_text(line, delay=0.1)
    root.after(1000, show_main_menu)


# Главное меню с информацией о текущем и лучшем стрике
def show_main_menu():
    clear_screen()
    global highscore
    append_text(f"Your current streak: {streak}")
    append_text(f"Your highest streak: {highscore}")
    btn_start = tk.Button(button_frame, text="Start Game", font=("Courier", 14),
                          command=start_game, bg="sandybrown", fg="black")
    btn_start.pack(side=tk.LEFT, padx=20, pady=10)
    btn_exit = tk.Button(button_frame, text="Exit", font=("Courier", 14),
                         command=exit_game, bg="sandybrown", fg="black")
    btn_exit.pack(side=tk.LEFT, padx=20, pady=10)


# Запуск игры: вместо "Shot" кнопка с новым текстом
def start_game():
    clear_screen()
    append_text('Game Started, press the button below to test your luck')
    btn_test = tk.Button(button_frame, text="Hey guy, ready to test your luck?", font=("Courier", 14),
                         command=do_shot, bg="sandybrown", fg="black")
    btn_test.pack(padx=20, pady=10)


# Логика выстрела
def do_shot():
    global streak, highscore
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
        root.after(total_delay + 500, lambda: append_text(f"Your streak was: {streak}"))
        root.after(total_delay + 1500, show_revive_menu)
    else:
        streak += 1
        if streak > highscore:
            highscore = streak
            save_highscore(highscore)
        append_text("You WIN!")
        append_text(f"You're lucky! Your streak: {streak} consecutive wins.")
        root.after(1500, show_main_menu)


# После смерти: медики реанимировали тебя и кнопка "Continue Game"
def show_revive_menu():
    clear_screen()
    append_text("Medics have revived you")
    btn_continue = tk.Button(button_frame, text="Continue Game", font=("Courier", 14),
                             command=show_main_menu, bg="sandybrown", fg="black")
    btn_continue.pack(side=tk.LEFT, padx=20, pady=10)
    global streak
    streak = 0


# Завершение игры с выводом ASCII-арта пистолета
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
    bg_image = Image.open(resource_path("wildwest.jpg"))
except Exception as e:
    print("Background image 'wildwest.jpg' not found. Make sure it exists in the working directory.")
    sys.exit(1)
bg_image = bg_image.resize((800, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Размещение фонового изображения
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создаем текстовый виджет (без переноса строк)
text_widget = tk.Text(root, bg="lightyellow", fg="orange", font=("Courier", 14),
                      bd=0, highlightthickness=0, wrap="none")
text_widget.place(relx=0.5, rely=0.5, anchor="center", width=750, height=400)
text_widget.tag_configure("center", justify="center")

# Фрейм для кнопок (располагаем внизу окна)
button_frame = tk.Frame(root, bg="lightyellow")
button_frame.place(relx=0.5, rely=0.9, anchor="center")

# Запуск описания бара, после которого появится кнопка "Enter bar"
show_description()
root.mainloop()
