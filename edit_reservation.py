import tkinter as tk
from tkinter import messagebox
# from database import update_reservation, read_single_reservation
from database import update_reservation, read_single_reservation

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.res_id = None
        
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}
        
        for idx, field in enumerate(fields):
            frame = tk.Frame(self)
            frame.pack(fill="x", padx=20, pady=5)
            label = tk.Label(frame, text=field, width=15)
            label.pack(side="left")
            entry = tk.Entry(frame, width=30)
            entry.pack(side="left")
            self.entries[field] = entry
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=20)
        update_btn = tk.Button(btn_frame, text="Update", command=self.update)
        update_btn.pack(side="left", padx=20)
        back_btn = tk.Button(btn_frame, text="Back", command=lambda: controller.show_frame("ReservationsPage"))
        back_btn.pack(side="left", padx=20)

    def load_reservation(self, res_id):
        self.res_id = res_id
        reservation = read_single_reservation(res_id)
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for field, value in zip(fields, reservation[1:]):
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, value)

    def update(self):
        if self.res_id:
            data = [self.entries[field].get() for field in self.entries]
            if all(data):
                update_reservation(self.res_id, data)
                messagebox.showinfo("Success", "Reservation updated!")
                self.controller.show_frame("ReservationsPage")
            else:
                messagebox.showerror("Error", "All fields are required")