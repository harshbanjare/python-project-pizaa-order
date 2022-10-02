from tkinter import *
from tkinter import ttk
from dbms import Orders


class CancelledOrders(Frame):

    def __init__(self, parent, *args, **kwargs):

        self._order_table = Orders()

        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("Cancelled Orders")
        self.parent.geometry("850x500")
        self.parent.resizable(False, False)

        self.subtitle = Label(self.parent, text="Cancelled Orders", font=(
            "Calibri", 28))
        self.subtitle.pack(ipadx=10, ipady=10)

        self.table_frame = Frame(self.parent)
        self.table_frame.pack(ipadx=10, ipady=10)

        self.table = ttk.Treeview(self.table_frame, columns=(
            "id", "name", "address", "pizza", "phone", "email"), show="headings")
        self.table.column("id", width=50, anchor="center")
        self.table.column("name", width=150, anchor="center")
        self.table.column("address", width=150, anchor="center")
        self.table.column("pizza", width=150, anchor="center")
        self.table.column("phone", width=150, anchor="center")
        self.table.column("email", width=150, anchor="center")

        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")

        self.table.heading("address", text="Address")
        self.table.heading("pizza", text="Pizza")
        self.table.heading("phone", text="Phone")
        self.table.heading("email", text="Email")

        self.table.pack()

        self._populate_table()

    def _populate_table(self):
        for order in self._order_table.get_cancelled_orders():
            self.table.insert("", "end", values=order)


if __name__ == "__main__":
    root = Tk()
    CancelledOrders(root)
    root.mainloop()
