import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output_label.config(text="Result: " + str(result))
    except:
        output_label.config(text="Error!")

# GUI window
root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30, font=("Arial", 16))
entry.pack(pady=10)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=5)

output_label = tk.Label(root, text="Result: ", font=("Arial", 14))
output_label.pack(pady=10)

root.mainloop()

