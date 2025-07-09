import tkinter as tk
from tkinter import ttk
from database import read_reservations, delete_reservation

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Flight", text="Flight")
        self.tree.heading("Departure", text="Departure")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat", text="Seat")
        self.tree.pack(fill="both", expand=True, padx=20, pady=20)
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=10)
        back_btn = tk.Button(btn_frame, text="Back", command=lambda: controller.show_frame("HomePage"))
        back_btn.pack(side="left", padx=20)
        edit_btn = tk.Button(btn_frame, text="Edit", command=self.edit_selected)
        edit_btn.pack(side="left", padx=20)
        delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_selected)
        delete_btn.pack(side="left", padx=20)

    def update_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in read_reservations():
            self.tree.insert("", "end", values=row)

    def edit_selected(self):
        selected = self.tree.selection()
        if selected:
            res_id = self.tree.item(selected[0])["values"][0]
            self.controller.show_frame("EditReservationPage")
            self.controller.frames["EditReservationPage"].load_reservation(res_id)

    def delete_selected(self):
        selected = self.tree.selection()
        if selected:
            res_id = self.tree.item(selected[0])["values"][0]
            delete_reservation(res_id)
            self.update_list()