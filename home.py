import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Flight Reservation System", font=("Arial", 24))
        label.pack(pady=40)
        book_btn = tk.Button(self, text="Book Flight", height=2, width=20, command=lambda: controller.show_frame("BookingPage"))
        book_btn.pack(pady=10)
        view_btn = tk.Button(self, text="View Reservations", height=2, width=20, command=lambda: controller.show_frame("ReservationsPage"))
        view_btn.pack(pady=10)