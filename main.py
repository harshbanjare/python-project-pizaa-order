from tkinter import ttk
from tkinter import *
from customer import Customer
from merchant import Merchant


class MainApplication(Frame):

    def __init__(self, parent, *args, **kwargs):

        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("Pizza Ordering and Delivery System")
        self.parent.geometry("800x250")
        self.parent.resizable(False, False)

        self.title = Label(
            self.parent, text="Pizza Order and Delivery System", font=("Calibri", 32))
        self.title.pack(ipadx=30, ipady=10)

        self.subtitle = Label(self.parent, text="Customer Or Merchant?", font=(
            "Calibri", 28), )
        self.subtitle.pack(ipadx=10, ipady=10)

        self.button_frame = Frame(self.parent)
        self.button_frame.pack(ipadx=10, ipady=10)

        self.customer_button = Button(self.button_frame, text="Customer", font=(
            "Calibri", 16), cursor="hand2", command=self.customer)
        self.customer_button.pack(side=LEFT, padx=10, pady=10)

        self.merchant_button = Button(self.button_frame, text="Merchant", font=(
            "Calibri", 16), cursor="hand2", command=self.merchant)
        self.merchant_button.pack(side=LEFT, padx=10, pady=10)

    def customer(self):
        root = Tk()
        Customer(root).pack(side="top", fill="both", expand=True)
        root.mainloop()

    def merchant(self):
        root = Tk()
        Merchant(root).pack(side="top", fill="both", expand=True)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
