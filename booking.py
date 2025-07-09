import tkinter as tk
from tkinter import messagebox
from database import create_reservation

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
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
        submit_btn = tk.Button(btn_frame, text="Submit", command=self.submit)
        submit_btn.pack(side="left", padx=20)
        back_btn = tk.Button(btn_frame, text="Back", command=lambda: controller.show_frame("HomePage"))
        back_btn.pack(side="left", padx=20)

    def submit(self):
        data = [self.entries[field].get() for field in self.entries]
        if all(data):
            create_reservation(tuple(data))
            messagebox.showinfo("Success", "Reservation created!")
            for entry in self.entries.values():
                entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields are required")