import tkinter as tk
from tkinter import messagebox
from agent import search_flights

def find_flights():
    source = entry_source.get()
    destination = entry_destination.get()

    result_box.delete(0, tk.END)

    if not source or not destination:
        messagebox.showwarning("Input Error", "Please enter both cities")
        return

    flights = search_flights(source, destination)

    if not flights:
        result_box.insert(tk.END, "❌ No flights found")
    else:
        for f in flights:
            result_box.insert(tk.END, f"{f['airline']} ✈️  ${f['price']}")

def book_selected():
    selected = result_box.curselection()
    if selected:
        flight = result_box.get(selected)
        messagebox.showinfo("Booking Confirmed", f"✅ {flight} booked!")

# 🎨 MAIN WINDOW
root = tk.Tk()
root.title("✈️ Talha Airline Agent")
root.geometry("420x500")
root.configure(bg="#0f172a")  # dark background

# 🎯 TITLE
title = tk.Label(root, text="✈️ Talha Airline Booking System", 
                 font=("Arial", 16, "bold"), 
                 bg="#0f172a", fg="#38bdf8")
title.pack(pady=15)

# 🎯 INPUT FIELDS
tk.Label(root, text="From", bg="#0f172a", fg="white").pack()
entry_source = tk.Entry(root, font=("Arial", 12), width=25)
entry_source.pack(pady=5)

tk.Label(root, text="To", bg="#0f172a", fg="white").pack()
entry_destination = tk.Entry(root, font=("Arial", 12), width=25)
entry_destination.pack(pady=5)

# 🎨 SEARCH BUTTON
search_btn = tk.Button(root, text="🔍 Search Flights",
                       bg="#22c55e", fg="white",
                       font=("Arial", 11, "bold"),
                       padx=10, pady=5,
                       command=find_flights)
search_btn.pack(pady=15)

# 🎯 RESULT BOX
result_box = tk.Listbox(root, width=45, height=10,
                        bg="#1e293b", fg="white",
                        font=("Arial", 10))
result_box.pack(pady=10)

# 🎨 BOOK BUTTON
book_btn = tk.Button(root, text="✈️ Book Flight",
                     bg="#3b82f6", fg="white",
                     font=("Arial", 11, "bold"),
                     padx=10, pady=5,
                     command=book_selected)
book_btn.pack(pady=10)

# 🎯 FOOTER
footer = tk.Label(root, text="Powered by Python AI Agent",
                  bg="#0f172a", fg="#94a3b8",
                  font=("Arial", 9))
footer.pack(pady=10)

# RUN APP
root.mainloop()
