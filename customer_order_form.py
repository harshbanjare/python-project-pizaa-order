from tkinter import ttk
from tkinter import *
from dbms import Orders


class CustomerOrderForm(Frame):

    def __init__(self, parent, *args, **kwargs):

        self._order_table = Orders()

        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("Order Pizza")
        self.parent.geometry("750x500")
        self.parent.resizable(False, False)

        self.name_var = StringVar()
        self.phone_var = StringVar()
        self.address_var = StringVar()
        self.pizza_var = StringVar()
        self.email_var = StringVar()
        self.id_var = self._order_table.get_next_order_id()

        self.subtitle = Label(self.parent, text="Order A pizza", font=(
            "Calibri", 28))
        self.subtitle.pack(ipadx=10, ipady=10)

        self.form_frame = Frame(self.parent)
        self.form_frame.pack(ipadx=10, ipady=10)

        self.id_label = Label(self.form_frame, text="ID",
                              font=("Calibri", 18), justify=LEFT, anchor="w")
        self.id_label.grid(sticky=W, row=0, column=0, padx=10, pady=10)

        self.id_value = Label(self.form_frame, bg='#696969', width=20,
                              text=self.id_var, font=("Calibri", 18))
        self.id_value.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = Label(self.form_frame, text="Name", font=(
            "Calibri", 18), justify=LEFT, anchor="w").grid(sticky=W, row=1, column=0, padx=10, pady=5)
        self.name_entry = Entry(self.form_frame, font=(
            "Calibri", 18), textvariable=self.name_var)
        self.name_entry.grid(
            row=1, column=1, padx=10, pady=5)

        self.phone_label = Label(self.form_frame, text="Phone", font=(
            "Calibri", 18), justify=LEFT, anchor="w").grid(sticky=W, row=2, column=0, padx=10, pady=5)
        self.phone_entry = Entry(self.form_frame, font=(
            "Calibri", 18), textvariable=self.phone_var)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = Label(self.form_frame, text="Address", font=(
            "Calibri", 16), justify=LEFT, anchor='w').grid(sticky=W, row=3, column=0, padx=10, pady=5)
        self.address_entry = Entry(self.form_frame, font=(
            "Calibri", 18), textvariable=self.address_var)
        self.address_entry.grid(
            row=3, column=1, padx=10, pady=5)
        self.email_label = Label(self.form_frame, text="Email", font=(
            "Calibri", 18), justify=LEFT, anchor="w").grid(sticky=W, row=4, column=0, padx=10, pady=5)
        self.email_entry = Entry(self.form_frame, font=(
            "Calibri", 18), textvariable=self.email_var)
        self.email_entry.grid(
            row=4, column=1, padx=10, pady=5)

        self.pizza_label = Label(self.form_frame, text="Pizza Type:", font=(
            "Calibri", 18), justify=LEFT, anchor="w").grid(sticky=W, row=5, column=0, padx=10, pady=5)

        self.pizza_combo = ttk.Combobox(
            self.form_frame, font=("Calibri", 16), width=20, textvariable=self.pizza_var)
        self.pizza_combo['values'] = (
            "Small", "Medium", "Large", "Extra Large", "Family")
        self.pizza_combo.grid(row=5, column=1, padx=10, pady=5)
        self.pizza_combo.current(0)

        self.submit_button = Button(self.parent, text="Submit", font=(
            "Calibri", 16), command=self.submit_order)
        self.submit_button.pack(ipadx=10, ipady=10)

        self.order_status_label = Label(self.parent, text=" ", font=(
            "Calibri", 18), justify=LEFT, anchor="w")
        self.order_status_label.pack(ipadx=10, ipady=10)

    def submit_order(self):

        order_success = self._order_table.create_order(
            int(self.id_var), self.name_var.get(), self.email_var.get(), self.phone_var.get(), self.address_var.get(), self.pizza_var.get())

        if order_success:
            self.id_var = self._order_table.get_next_order_id()
            self.id_value.config(text=self.id_var)
            self.name_entry.config(state="disabled")
            self.phone_entry.config(state="disabled")
            self.address_entry.config(state="disabled")
            self.email_entry.config(state="disabled")
            self.pizza_combo.config(state="disabled")
            self.submit_button.config(state="disabled")
            self.order_status_label.config(
                text="Order Submitted Successfully", fg="green")
        else:
            self.order_status_label.config(
                text="Order Submission Failed", fg="red")


if __name__ == "__main__":
    root = Tk()
    CustomerOrderForm(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
