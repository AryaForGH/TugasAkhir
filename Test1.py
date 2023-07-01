import tkinter as tk 

def hitung():
    try:
        angka1 = float(entry_angka1.get())
        angka2 = float(entry_angka2.get())
        operator = entry_operator.get()

        if operator == '+':
            hasil = angka1 + angka2

        elif operator == '-':
            hasil = angka1 - angka2

        elif operator == '*':
            hasil = angka1 * angka2

        elif operator == '/':
            hasil = angka1 / angka2

        else:
            hasil = "Operasi Tidak Valid"

        label_hasil.config(text="Hasil : " + str(hasil))
    except ValueError:
        label_hasil.config(text="Masukan Tidak Valid")

root = tk.Tk()
root.title("Kalkulator Kel 2")

label_angka1 = tk.Label(root, text="Angka 1 : ")
label_angka1.pack()
entry_angka1 = tk.Entry(root)
entry_angka1.pack()

label_operator = tk.Label(root, text="Operator (+,-,*,/) : ")
label_operator.pack()
entry_operator = tk.Entry(root)
entry_operator.pack()

label_angka2 = tk.Label(root, text="Angka 2 : ")
label_angka2.pack()
entry_angka2 = tk.Entry(root)
entry_angka2.pack()

button_hitung = tk.Button(root, text="Hitung", command=hitung)
button_hitung.pack()

label_hasil = tk.Label(root, text="Hasil")
label_hasil.pack()

root.mainloop()