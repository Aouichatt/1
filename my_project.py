https://gitimport tkinter as tk
from tkinter import ttk, Entry, Label, Button, StringVar, messagebox
import requests

def generate_m3u_link():
    m3u_link = f"http://{server_entry.get()}:{port_entry.get()}/get.php?username={username_entry.get()}&password={password_entry.get()}&type=m3u_plus&output=ts"
    result_var.set(m3u_link)

def test_and_download():
    link = result_var.get()
    if not link:
        messagebox.showerror("Error", "Please generate a link first!")
        return

    try:
        response = requests.get(link)
        response.raise_for_status()
        
        with open("playlist.m3u", "wb") as f:
            f.write(response.content)
        
        messagebox.showinfo("Success", "Downloaded successfully!")

    except requests.RequestException:
        messagebox.showerror("Error", "Failed to fetch the link!")

app = tk.Tk()
app.title('M3U Link Generator')

# ... (rest of your code remains unchanged) ...

ttk.Button(app, text="Test & Download", command=test_and_download).grid(row=7, column=0, columnspan=2, pady=10)

app.mainloop()hub.com/Aouichatt/1.git