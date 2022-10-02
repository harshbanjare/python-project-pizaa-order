from tkinter import ttk
from tkinter import *
from dbms import Orders


class ReceiveOrderForm(Frame):

    def __init__(self, parent, *args, **kwargs):

        self._order_table = Orders()

        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("Receive Order")
        self.parent.geometry("750x250")
        self.parent.resizable(False, False)

        self.id_var = StringVar()

        self.subtitle = Label(
            self.parent, text="Receive Order", font=("Calibri", 28))
        self.subtitle.pack(ipadx=10, ipady=10)

        self.form_frame = Frame(self.parent)
        self.form_frame.pack(ipadx=10, ipady=10)

        self.id_label = Label(self.form_frame, text="ID", font=(
            "Calibri", 18), justify=LEFT, anchor="w")
        self.id_label.grid(sticky=W, row=0, column=0, padx=10, pady=10)

        self.id_entry = Entry(self.form_frame, font=(
            "Calibri", 18), textvariable=self.id_var)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.receive_button = Button(self.form_frame, text="Receive Order", font=(
            "Calibri", 18), command=self.receive_order)
        self.receive_button.grid(
            row=1, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = Label(
            self.form_frame, text="", font=("Calibri", 18))
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def receive_order(self):
        order_id = self.id_var.get()
        if self._order_table.get_order_status(order_id) == "PENDING":
            if self._order_table.update_status(order_id, "DELIVERED"):
                self.result_label.config(text="Order Received")
                self.result_label.config(fg="green")
                self.id_entry.config(state="disabled")
            else:
                self.result_label.config(text="Order Not Found")
                self.result_label.config(fg="red")
        else:
            self.result_label.config(text="Order Not Found")
            self.result_label.config(fg="red")


if __name__ == "__main__":
    root = Tk()
    ReceiveOrderForm(root)
    root.mainloop()
