from re import L
from tkinter import ttk
from tkinter import *


class CustomerOrderForm(Frame):

    def __init__(self, parent, *args, **kwargs):

        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("Order Pizza")
        self.parent.geometry("750x600")
        self.parent.resizable(False, False)

        self.subtitle = Label(self.parent, text="Order A pizza", font=(
            "Calibri", 28))
        self.subtitle.pack(ipadx=10, ipady=10)

        self.form_frame = Frame(self.parent)
        self.form_frame.pack(ipadx=10, ipady=10)

        self.id_label = Label(self.form_frame, text="ID",
                              font=("Calibri", 18), justify=LEFT, anchor="w")
        self.id_label.grid(sticky=W, row=0, column=0, padx=10, pady=10)

        self.id_value = Label(self.form_frame, bg='#696969', width=20,
                              text="1", font=("Calibri", 18))
        self.id_value.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = Label(self.form_frame, text="Name", font=(
            "Calibri", 18), justify=LEFT, anchor="w").grid(sticky=W, row=1, column=0, padx=10, pady=5)
        self.name_entry = Entry(self.form_frame, font=("Calibri", 18)).grid(
            row=1, column=1, padx=10, pady=5)

        self.phone_label = Label(self.form_frame, text="Phone", font=(
            "Calibri", 18), justify=LEFT, anchor="w").grid(sticky=W, row=2, column=0, padx=10, pady=5)
        self.phone_entry = Entry(self.form_frame, font=(
            "Calibri", 18)).grid(row=2, column=1, padx=10, pady=5)

        self.address_label = Label(self.form_frame, text="Address", font=(
            "Calibri", 16), justify=LEFT, anchor='w').grid(sticky=W, row=3, column=0, padx=10, pady=5)
        self.address_entry = Entry(self.form_frame, font=("Calibri", 18)).grid(
            row=3, column=1, padx=10, pady=5)
        self.email_label = Label(self.form_frame, text="Email", font=(
            "Calibri", 18), justify=LEFT, anchor="w").grid(sticky=W, row=4, column=0, padx=10, pady=5)
        self.email_entry = Entry(self.form_frame, font=("Calibri", 18)).grid(
            row=4, column=1, padx=10, pady=5)


if __name__ == "__main__":
    root = Tk()
    CustomerOrderForm(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
