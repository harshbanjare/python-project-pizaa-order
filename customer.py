from tkinter import ttk
from tkinter import *
from customer_order_form import CustomerOrderForm
from customer_cancel_form import OrderCancelForm
from customer_receive_order_form import ReceiveOrderForm
from customer_track_order import TrackOrder


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
            self.button_frame, text="Order Pizza", cursor="hand2", font=("Calibri", 18), command=self.orderForm)
        self.order_pizza_button.pack(side=LEFT, padx=10, pady=10)

        self.track_order_button = Button(
            self.button_frame, text="Track Order", cursor="hand2", font=("Calibri", 18), command=self.trackOrder)
        self.track_order_button.pack(side=LEFT, padx=10, pady=10)

        self.cancel_order_button = Button(
            self.button_frame, text="Cancel Order", cursor="hand2", font=("Calibri", 18), command=self.cancelForm)
        self.cancel_order_button.pack(side=LEFT, padx=10, pady=10)

        self.receive_order_button = Button(
            self.button_frame, text="Receive Order", cursor="hand2", font=("Calibri", 18), command=self.receiveOrder)
        self.receive_order_button.pack(side=LEFT, padx=10, pady=10)

    def orderForm(self):
        root = Toplevel(self.parent)
        CustomerOrderForm(root).pack(side="top", fill="both", expand=True)
        root.mainloop()

    def cancelForm(self):
        root = Toplevel(self.parent)
        OrderCancelForm(root).pack(side="top", fill="both", expand=True)
        root.mainloop()

    def receiveOrder(self):
        root = Toplevel(self.parent)
        ReceiveOrderForm(root).pack(side="top", fill="both", expand=True)
        root.mainloop()

    def trackOrder(self):
        root = Toplevel(self.parent)
        TrackOrder(root).pack(side="top", fill="both", expand=True)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    Customer(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
