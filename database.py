import sqlite3

def create_table():
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reservations 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT, 
                 flight_number TEXT, 
                 departure TEXT, 
                 destination TEXT, 
                 date TEXT, 
                 seat_number TEXT)''')
    conn.commit()
    conn.close()

create_table()


def read_single_reservation(res_id):
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute("SELECT * FROM reservations WHERE id=?", (res_id,))
    row = c.fetchone()
    conn.close()
    return row

def create_reservation(data):
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute('''INSERT INTO reservations 
                 (name, flight_number, departure, destination, date, seat_number) 
                 VALUES (?, ?, ?, ?, ?, ?)''', data)
    conn.commit()
    conn.close()

def read_reservations():
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute("SELECT * FROM reservations")
    rows = c.fetchall()
    conn.close()
    return rows

def update_reservation(res_id, data):
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute('''UPDATE reservations SET 
                 name=?, flight_number=?, departure=?, 
                 destination=?, date=?, seat_number=? 
                 WHERE id=?''', (*data, res_id))
    conn.commit()
    conn.close()

def delete_reservation(res_id):
    conn = sqlite3.connect('flights.db')
    c = conn.cursor()
    c.execute("DELETE FROM reservations WHERE id=?", (res_id,))
    conn.commit()
    conn.close()