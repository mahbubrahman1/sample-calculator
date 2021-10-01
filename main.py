from tkinter import *

# color
OFF_BLUE = "#F1F7fA"
DARK_NAVY = "#314C66"
LIGHT_BLUE = "#74B5F2"
WHITE = "#F8FAFF"

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.window.iconbitmap("icon.ico")

        self.total_ex = ""
        self.current_ex = ""

        self.display_frame = self.create_display_frame()

        self.total_lebel, self.label = self.create_display_label()

        self.digits = {
            7: (1, 1),
            8: (1, 2),
            9: (1, 3),
            4: (2, 1),
            5: (2, 2),
            6: (2, 3),
            1: (3, 1),
            2: (3, 2),
            3: (3, 3),
            0: (4, 2),
            ".": (4, 1),
        }
        self.operations = {"/": "\u00f7", "*": "\u00d7", "-": "-", "+": "+"}
        self.button_frame = self.create_button_frame()

        self.button_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)

        self.create_digit_button()
        self.create_operator_buttons()
        self.create_special_button()

    def create_special_button(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_display_label(self):
        total_label = Label(
            self.display_frame,
            text=self.total_ex,
            anchor=E,
            bg=WHITE,
            fg=DARK_NAVY,
            padx=24,
            font=("Arial 16"),
        )
        total_label.pack(expand=True, fill="both")

        lbl = Label(
            self.display_frame,
            text=self.current_ex,
            anchor=E,
            bg=WHITE,
            fg=DARK_NAVY,
            padx=24,
            font=("Arial 40 bold"),
        )
        lbl.pack(expand=True, fill="both")

        return total_label, lbl

    def create_display_frame(self):
        frm = Frame(self.window, height=221, bg="light gray")
        frm.pack(expand=True, fill="both")
        return frm

    def add_to_ex(self, value):
        self.current_ex += str(value)
        self.update_label()

    def create_digit_button(self):
        for digit, grid_value in self.digits.items():
            butt = Button(
                self.button_frame,
                text=str(digit),
                bg=WHITE,
                fg=DARK_NAVY,
                font=("Arial 24 bold"),
                borderwidth=0,
                command=lambda x=digit: self.add_to_ex(x),
            )
            butt.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

    def append_operator(self, operator):
        self.current_ex += operator
        self.total_ex += self.current_ex
        self.current_ex = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            butt = Button(
                self.button_frame,
                text=symbol,
                bg=OFF_BLUE,
                fg=DARK_NAVY,
                font=("arial 20"),
                borderwidth=0,
                command=lambda x=operator: self.append_operator(x),
            )
            butt.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def clear(self):
        self.current_ex = ""
        self.total_ex = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        butt = Button(
            self.button_frame,
            text="C",
            bg=OFF_BLUE,
            fg=DARK_NAVY,
            font=("arial 20"),
            borderwidth=0,
            command=self.clear,
        )
        butt.grid(row=0, column=1, columnspan=3, sticky=NSEW)

    def evalue(self):
        self.total_ex += self.current_ex
        self.update_total_label()

        try:
            self.current_ex = str(eval(self.total_ex))
            self.total_ex = ""
        except Exception as e:
            self.current_ex = "Error"
        finally:
            self.update_label()

        self.update_label()

    def create_equals_button(self):
        butt = Button(
            self.button_frame,
            text="=",
            bg=LIGHT_BLUE,
            fg=DARK_NAVY,
            font=("arial 20"),
            borderwidth=0,
            command=self.evalue,
        )
        butt.grid(row=4, column=3, columnspan=2, sticky=NSEW)

    def create_button_frame(self):
        frm = Frame(self.window)
        frm.pack(expand=True, fill="both")
        return frm

    def update_total_label(self):
        ex = self.total_ex
        for operator, symbol in self.operations.items():
            ex = ex.replace(operator, f" {symbol} ")
        self.total_lebel.config(text=ex)

    def update_label(self):
        self.label.config(text=self.current_ex[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()