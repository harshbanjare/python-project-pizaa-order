from tkinter import *
from tkinter import ttk
# from dbms import Orders
from mongo_db import Orders


class TrackOrder(Frame):

    def __init__(self, parent, *args, **kwargs):

        Frame.__init__(self, parent, *args, **kwargs)

        self._order_table = Orders()
        self.parent = parent
        self.parent.title("Track Order")
        self.parent.geometry("750x300")
        self.parent.resizable(False, False)

        self.id_var = StringVar()

        self.subtitle = Label(self.parent, text="Track Order", font=(
            "Calibri", 28))
        self.subtitle.pack(ipadx=10, ipady=10)

        self.form_frame = Frame(self.parent)
        self.form_frame.pack(ipadx=10, ipady=10)

        self.id_entry = Entry(
            self.form_frame, textvariable=self.id_var)
        self.id_entry.pack(ipadx=10, ipady=10, side=LEFT)

        self.track_button = Button(
            self.form_frame, text="Track", command=self.track_order)
        self.track_button.pack(ipadx=10, ipady=10, side=LEFT)

        self.status_progress_bar = ttk.Progressbar(
            self.parent, orient=HORIZONTAL, length=500, mode='determinate')
        self.status_progress_bar.pack(ipadx=10, ipady=10)

        self.status_frame = Frame(self.parent)
        self.status_frame.pack(ipadx=10, ipady=10)

        self.status_label = Label(
            self.status_frame, text="Status: ", font=("Calibri", 18))
        self.status_label.pack(ipadx=10, ipady=10, side=LEFT)

        self.status_value = Label(
            self.status_frame, text="", font=("Calibri", 18))
        self.status_value.pack(ipadx=10, ipady=10, side=LEFT)

    def track_order(self):
        order_id = self.id_var.get()
        order = self._order_table.get_order_status(order_id)
        if order == "PENDING":
            self.status_progress_bar['value'] = 30
            self.status_value.config(text=order)
            self.status_value.config(fg="orange")
        elif order == "IN TRANSIT":
            self.status_progress_bar['value'] = 60
            self.status_value.config(text=order)
            self.status_value.config(fg="blue")
        elif order == "DELIVERED":
            self.status_progress_bar['value'] = 100
            self.status_value.config(text=order)
            self.status_value.config(fg="green")
        elif order == "CANCELLED":
            self.status_progress_bar['value'] = 1
            self.status_value.config(text=order)
            self.status_value.config(fg="red")
        else:
            self.status_progress_bar['value'] = 1
            self.status_value.config(text="Order Not Found")
            self.status_value.config(fg="red")


if __name__ == "__main__":
    root = Tk()
    TrackOrder(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
