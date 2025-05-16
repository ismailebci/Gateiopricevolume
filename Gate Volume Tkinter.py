# app.py
import tkinter as tk
from tkinter import ttk
from gate_api import ApiClient, SpotApi, Configuration
from config import API_KEY, API_SECRET

# Gate.io API konfigürasyonu
configuration = Configuration(key=API_KEY, secret=API_SECRET)
api_client = ApiClient(configuration)
spot_api = SpotApi(api_client)

PAGE_SIZE = 50
current_page = 0

def fetch_markets():
    markets = spot_api.list_tickers()
    filtered_markets = [m for m in markets if float(m.base_volume) > 0]
    return sorted(filtered_markets, key=lambda x: float(x.base_volume))

def update_tree():
    global current_page
    for item in tree.get_children():
        tree.delete(item)

    min_vol = float(min_volume_entry.get() or 0)
    max_vol = float(max_volume_entry.get() or float('inf'))

    filtered = [
        c for c in fetch_markets()
        if min_vol <= float(c.base_volume) <= max_vol and "USDT" in c.currency_pair
    ]

    total_pages = (len(filtered) + PAGE_SIZE - 1) // PAGE_SIZE
    start, end = current_page * PAGE_SIZE, (current_page + 1) * PAGE_SIZE

    for coin in filtered[start:end]:
        last = float(coin.last)
        high = float(coin.high_24h)
        low = float(coin.low_24h)
        change = ((last - low) / low) * 100 if last > 0 and low > 0 else 0
        color = "green" if change > 0 else "red"
        tree.insert("", tk.END, values=(
            coin.currency_pair, f"{last:.4f} USD", f"{coin.base_volume} USD",
            f"{high} USD", f"{low} USD", f"{change:.2f}%"), tags=(color,))

    page_label.config(text=f"Sayfa: {current_page + 1}/{total_pages}")
    root.after(5000, update_tree)

def next_page():
    global current_page
    current_page += 1
    update_tree()

def previous_page():
    global current_page
    if current_page > 0:
        current_page -= 1
    update_tree()

def sort_tree(col, reverse):
    data = [(tree.set(c, col), c) for c in tree.get_children()]
    data.sort(reverse=reverse)
    for idx, (val, item) in enumerate(data):
        tree.move(item, '', idx)
    tree.heading(col, command=lambda: sort_tree(col, not reverse))

# Tkinter arayüzü
root = tk.Tk()
root.title("Gate.io Hacim Filtreleme")
root.configure(bg="black")

frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

# Hacim aralığı giriş
for i, (label, var) in enumerate([("Minimum Hacim:", "min_volume_entry"), ("Maksimum Hacim:", "max_volume_entry")]):
    tk.Label(frame, text=label, bg="black", fg="white").grid(row=i, column=0)
    entry = tk.Entry(frame)
    entry.grid(row=i, column=1)
    globals()[var] = entry

tk.Button(root, text="Ara", command=update_tree).pack(pady=10)
tk.Button(root, text="Önceki", command=previous_page).pack(side=tk.LEFT, padx=5, pady=10)
tk.Button(root, text="Sonraki", command=next_page).pack(side=tk.LEFT, padx=5, pady=10)

tree = ttk.Treeview(root, columns=("Name", "Price", "Volume", "High", "Low", "24h Change"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col, command=lambda c=col: sort_tree(c, False))
    tree.column(col, width=120)
tree.tag_configure("green", foreground="green")
tree.tag_configure("red", foreground="red")
tree.pack(expand=True, fill=tk.BOTH)

page_label = tk.Label(root, bg="black", fg="white")
page_label.pack(pady=5)

update_tree()
root.mainloop()
