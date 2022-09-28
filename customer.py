from tkinter import ttk
from tkinter import *


class Customer(Frame):

    def __init__(self, parent, *args, **kwargs):

        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("Customer")
        self.parent.geometry("750x200")
        self.parent.resizable(False, False)

        self.subtitle = Label(self.parent, text="Please Select an Option.", font=(
            "Calibri", 28), )
        self.subtitle.pack(ipadx=10, ipady=10)

        self.button_frame = Frame(self.parent)
        self.button_frame.pack(ipadx=10, ipady=10)

        self.order_pizza_button = Button(
            self.button_frame, text="Order Pizza", cursor="hand2", font=("Calibri", 18), command=self)
        self.order_pizza_button.pack(side=LEFT, padx=10, pady=10)

        self.track_order_button = Button(
            self.button_frame, text="Track Order", cursor="hand2", font=("Calibri", 18), command=self)
        self.track_order_button.pack(side=LEFT, padx=10, pady=10)

        self.back_button = Button(
            self.button_frame, text="Cancel Order", cursor="hand2", font=("Calibri", 18), command=self)
        self.back_button.pack(side=LEFT, padx=10, pady=10)


if __name__ == "__main__":
    root = Tk()
    Customer(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
