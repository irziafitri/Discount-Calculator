import tkinter as tk

def calculate_discount():
    try:
        harga = float(entry_harga.get())
        diskon = float(entry_diskon.get())
        
        harga_akhir = harga - (harga * diskon / 100)
        
        hasil_formatted = f"Rp {int(harga_akhir):,}".replace(",", ".")
        
        label_hasil.config(text=hasil_formatted)
        
    except ValueError:
        label_hasil.config(text="Input tidak valid!")

# buat window
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("350x350")
root.configure(bg="#f0f0f0")

# judul
label_judul = tk.Label(root, text="Discount Calculator", 
                      font=("Arial", 18, "bold"),
                      bg="#f0f0f0")
label_judul.pack(pady=20)

# input harga
frame_harga = tk.Frame(root, bg="#f0f0f0")
frame_harga.pack(pady=10)

label_harga = tk.Label(frame_harga, text="Original Price:", 
                      font=("Arial", 12),
                      bg="#f0f0f0")
label_harga.pack()

entry_harga = tk.Entry(frame_harga, font=("Arial", 14), 
                      width=15, justify="center",
                      bd=2, relief="groove")
entry_harga.pack(pady=5)

# input diskon
frame_diskon = tk.Frame(root, bg="#f0f0f0")
frame_diskon.pack(pady=10)

label_diskon = tk.Label(frame_diskon, text="Discount (%):", 
                       font=("Arial", 12),
                       bg="#f0f0f0")
label_diskon.pack()

entry_diskon = tk.Entry(frame_diskon, font=("Arial", 14), 
                       width=15, justify="center",
                       bd=2, relief="groove")
entry_diskon.pack(pady=5)

# tombol hitung
btn_hitung = tk.Button(root, text="Calculate", 
                      command=calculate_discount,
                      font=("Arial", 12, "bold"),
                      bg="#84A885",
                      fg="white",
                      width=12,
                      height=1,
                      bd=0,
                      relief="raised")
btn_hitung.pack(pady=20)

# frame hasil
frame_hasil = tk.Frame(root, bg="#f0f0f0")
frame_hasil.pack()

label_hasil_teks = tk.Label(frame_hasil, text="Final Price:", 
                           font=("Arial", 12),
                           bg="#f0f0f0")
label_hasil_teks.pack()

# hasil
label_hasil = tk.Label(frame_hasil, text="", 
                      font=("Arial", 16, "bold"),
                      fg="#84A885",
                      bg="#f0f0f0")
label_hasil.pack(pady=5) 


# Jalankan aplikasi
root.mainloop()