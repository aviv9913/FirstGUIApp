import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

button = tk.Button(frame, text="Test button", bg="gray", fg='black')
#button.pack(side="left", fill="x", expand=True)
button.grid(row=0, column=0)

label = tk.Label(frame, text="This is a label")
label.grid(row=1, column=1)

entry = tk.Entry(frame, bg="green")
entry.grid(row=1, column=1)
root.mainloop()
