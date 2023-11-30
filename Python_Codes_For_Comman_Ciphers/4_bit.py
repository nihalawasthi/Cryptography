#1 4 Bit – 64 Bit gate operation with diagram 


import tkinter as tk

def invert_binary(binary_str):
    inverted = "".join(["0" if bit == "1" else "1" for bit in binary_str])
    return inverted

def draw_box_with_lines(binary_str):
    canvas.delete("all") 
    canvas.create_rectangle(100, 50, 250, 175, outline="black") 
    
    for i, bit in enumerate(binary_str):
        y = 75 + i * 25
        line_color = "black" if bit == "1" else "red"
        canvas.create_line(50, y, 100, y, fill=line_color)
        canvas.create_text(0, y, text=bit, anchor="e")
    
    inverted_binary = invert_binary(binary_str)
    
    for i, bit in enumerate(inverted_binary):
        y = 75 + i * 25
        line_color = "black" if bit == "1" else "red"
        canvas.create_line(250, y, 300, y, fill=line_color)
        canvas.create_text(328, y, text=bit, anchor="w")

def ok_button_click():
    binary_str = binary_entry.get()
    if len(binary_str) == 4 and binary_str.isdigit() and all(bit in "01" for bit in binary_str):
        draw_box_with_lines(binary_str)
        result_label.config(text="")
    else:
        result_label.config(text="Invalid input! Please enter a 4-bit binary number.")

root = tk.Tk()
root.title("Binary Inverter")

binary_label = tk.Label(root, text="Enter a 4-bit binary number")
binary_label.pack()

binary_entry = tk.Entry(root)
binary_entry.pack()

ok_button = tk.Button(root, text="OK", command=ok_button_click)
ok_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

root.mainloop()
