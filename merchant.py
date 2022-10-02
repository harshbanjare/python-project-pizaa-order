from tkinter import ttk
from tkinter import *
from merchant_new_orders import NewOrders
from merchant_cancelled_orders import CancelledOrders
from merchant_served_orders import ServedOrders


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
        self.upper_button_frame.pack(ipadx=10, ipady=30)

        self.order_pizza_button = Button(
            self.upper_button_frame, text="New Pizza Order", cursor="hand2", font=("Calibri", 18), command=self.new_orders)
        self.order_pizza_button.pack(side=LEFT, padx=0, pady=0)

        self.track_order_button = Button(
            self.upper_button_frame, text="Cancelled Order", cursor="hand2", font=("Calibri", 18), command=self.cancelled_orders)
        self.track_order_button.pack(side=LEFT, padx=0, pady=0)

        self.served_order_button = Button(self.upper_button_frame, text="Served Order", font=(
            "Calibri", 18), command=self.served_orders, cursor="hand2")
        self.served_order_button.pack(side=LEFT, padx=0, pady=0)

    def new_orders(self):
        root = Toplevel(self.parent)
        NewOrders(root).pack(side="top", fill="both", expand=True)
        root.mainloop()

    def cancelled_orders(self):
        root = Toplevel(self.parent)
        CancelledOrders(root).pack(side="top", fill="both", expand=True)
        root.mainloop()

    def served_orders(self):
        root = Toplevel(self.parent)
        ServedOrders(root).pack(side="top", fill="both", expand=True)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    Merchant(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
