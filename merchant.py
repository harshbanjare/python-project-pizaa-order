from tkinter import ttk
from tkinter import *


class Merchant(Frame):

    def __init__(self, parent, *args, **kwargs):

        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("Merchant")
        self.parent.geometry("750x200")
        self.parent.resizable(False, False)

        self.subtitle = Label(self.parent, text="Please Select an Option.", font=(
            "Calibri", 28), )
        self.subtitle.pack(ipadx=10, ipady=10)

        self.upper_button_frame = Frame(self.parent)
        self.upper_button_frame.pack(ipadx=5, ipady=0)

        self.order_pizza_button = Button(
            self.upper_button_frame, text="New Pizza Order", cursor="hand2", font=("Calibri", 18), command=self)
        self.order_pizza_button.pack(side=LEFT, padx=0, pady=0)

        self.track_order_button = Button(
            self.upper_button_frame, text="Cancelled Order", cursor="hand2", font=("Calibri", 18), command=self)
        self.track_order_button.pack(side=LEFT, padx=0, pady=0)

        self.lower_button_frame = Frame(self.parent)
        self.lower_button_frame.pack(ipadx=5, ipady=0)

        self.served_order_button = Button(self.lower_button_frame, text="Served Order", font=(
            "Calibri", 18), command=self, cursor="hand2")
        self.served_order_button.pack(side=LEFT, padx=0, pady=0)

        self.pending_order_button = Button(
            self.lower_button_frame, text="Pending Order", cursor="hand2", font=("Calibri", 18), command=self)
        self.pending_order_button.pack(side=LEFT, padx=0, pady=0)


if __name__ == "__main__":
    root = Tk()
    Merchant(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
