import tkinter as tk

root = tk.Tk()
root.title("Sample Window")
root.geometry("300x200")

label = tk.Label(root, text="Hello, World!")
label.pack()

root.mainloop()