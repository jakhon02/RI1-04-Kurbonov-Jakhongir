import tkinter as tk
from tkinter import messagebox

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
entry_font = ('Arial', 12, 'bold')
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

class OnlineShop(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {}
        for F in (LoginWindow, MainWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginWindow")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class LoginWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#334353')

        # метка для поля ввода имени
        username_label = tk.Label(self, text='Имя пользователя', font=label_font, **base_padding,
                                  bg='#3591CD')
        username_label.pack(**base_padding)
        self.controller.configure(background='#334353')
        # поле ввода имени
        self.username_entry = tk.Entry(self, bg='#fff', fg='#444', font=font_entry)
        self.username_entry.pack()

        # метка для поля ввода пароля
        password_label = tk.Label(self, text='Пароль', font=label_font, **base_padding,
                                  bg='#3591CD')
        password_label.pack(**base_padding)

        # поле ввода пароля
        self.password_entry = tk.Entry(self, show='*', bg='#fff', fg='#444', font=font_entry)
        self.password_entry.pack()

        # кнопка отправки формы
        self.send_btn = tk.Button(self, text='Войти', font='bold',  bg='#3591CD',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.check_password())
        self.send_btn.pack(**base_padding)

    def check_password(self):
        if self.password_entry.get() == "1977" and self.username_entry.get() == "Alex":
            self.controller.show_frame("MainWindow")
        else:
            messagebox.showinfo("ERROR", "Неверный пароль или логин")


class MainWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#334353')

        self.dish_btn1 = tk.Button(self, text='Плов', font='bold',  bg='#3591CD',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.click_button1())
        self.dish_btn2 = tk.Button(self, text='Лагман', font='bold',  bg='#3591CD',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.click_button2())
        self.dish_btn3 = tk.Button(self, text='Казан-кабоб', font='bold',  bg='#3591CD',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.click_button3())
        self.dish_btn4 = tk.Button(self, text='Нарын', font='bold',  bg='#3591CD',
                                  activebackground='#20B2AA', width=10,
                                   command=lambda: self.click_button4())

        self.dish_btn1.grid(row=0, column=0, padx=50, pady=10)
        self.dish_btn2.grid(row=0, column=1, padx=50, pady=10)
        self.dish_btn3.grid(row=1, column=0, padx=50, pady=10)
        self.dish_btn4.grid(row=1, column=1, padx=50, pady=10)

        self.order_btn = tk.Button(self, text="Заказать", font='bold',  bg='#3591CD',
                                  activebackground='#20B2AA', width=20,
                                   command=lambda: self.MsgBox())
        self.order_btn.grid(row=6, column=0, columnspan=2, pady=70)


        self.write_box = tk.Label(self, width=40, font=label_font, **base_padding,
                                  bg='#3591CD')
        self.write_box.grid(row=2, column=0, columnspan=2,)

        self.location_lb = tk.Label(self, text='Введите свою локацию', font=label_font, **base_padding,
                                  bg='#3591CD')
        self.location_lb.grid(row=4, column=0, columnspan=2, pady=15)
        self.message = tk.StringVar()
        self.location_en = tk.Entry(self, width=40, highlightthickness=10, font=entry_font,
                                    textvariable=self.message)
        self.location_en.grid(row=5, column=0, columnspan=2,)

    def MsgBox(self):
        messagebox.showinfo("Заказ принят!",  self.message.get())

    def click_button1(self):
        self.write_box.config(text="Рис, Морковь, Лук, Мясо, Масло")

    def click_button2(self):
        self.write_box.config(text="Домашняя лапша, Баранина, Морковь,\n Красный сладкий перец")

    def click_button3(self):
        self.write_box.config(text="Баранина на косточке, Картофель,\n Подсолнечное масло")

    def click_button4(self):
        self.write_box.config(text="Масло, Тмин, Чёрный перец, Казы, Тесто")

if __name__ == "__main__":
    app = OnlineShop()

    app.title("Интернет магазин")
    app.geometry("400x500")
    app.resizable(False, False)

    app.grid_columnconfigure(0, minsize=100)
    app.mainloop()