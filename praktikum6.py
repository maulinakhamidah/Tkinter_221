import tkinter as tk

def prediksi_prodi():
    hasil_label.config(text="Hasil Prediksi: Teknologi Informasi")
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("900x500")  #Ukuran jendela
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 18, "bold"))
judul_label.pack(pady=20)
input_frame = tk.Frame(root)  # untuk menampung sebuah wadah
input_frame.pack(pady=10)
entries = []
for i in range(10):
    row = i %  5       # 5 baris
    col = i // 5       # 2 kolom (0 atau 1)
    label = tk.Label(input_frame, text=f"Nilai MataPelajaran {i+1}:")
    label.grid(row=row, column=col*2, padx=5, pady=5, sticky="e")
    entry = tk.Entry(input_frame, width=10)
    entry.grid(row=row, column=col*2 + 1, padx=5, pady=5)
    entries.append(entry)
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi, bg="pink", font=("Times New Roman", 12))
prediksi_button.pack(pady=20)
hasil_label = tk.Label(root, text="Hasil Prediksi: ", font=("Times New Roman", 16), fg="black")
hasil_label.pack(pady=10)
# jalankan printahnya
root.mainloop()
  