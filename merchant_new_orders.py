from tkinter import ttk
from tkinter import *
from dbms import Orders


class NewOrders(Frame):

    def __init__(self, parent, *args, **kwargs):

        self._order_table = Orders()

        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.title("New Orders")
        self.parent.geometry("850x500")
        self.parent.resizable(False, False)

        self.subtitle = Label(self.parent, text="New Orders", font=(
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

        self.button_frame = Frame(self.parent)
        self.button_frame.pack(ipadx=10, ipady=10)

        self.cancel_button = Button(
            self.button_frame, text="Cancel", command=self._cancel_order)
        self.cancel_button.pack(side=LEFT, padx=0, pady=0)

        self.serve_button = Button(
            self.button_frame, text="Serve", command=self._serve_order)
        self.serve_button.pack(side=LEFT, padx=10, pady=10)

    def _populate_table(self):
        for order in self._order_table.get_pending_orders():
            self.table.insert("", "end", values=order)

    def _refresh_table(self):
        print("Refreshing table")
        self.table.delete(*self.table.get_children())
        self._populate_table()

    def _cancel_order(self):
        selected_item = self.table.selection()
        if selected_item:
            order_id = self.table.item(selected_item[0])["values"][0]
            self._order_table.update_status(order_id, "CANCELLED")
            self._refresh_table()

    def _serve_order(self):
        selected_item = self.table.selection()
        if selected_item:
            order_id = self.table.item(selected_item[0])["values"][0]
            self._order_table.update_status(order_id, "IN TRANSIT")
            self._refresh_table()


if __name__ == "__main__":
    root = Tk()
    NewOrders(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
