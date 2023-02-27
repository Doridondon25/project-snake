import tkinter as tk

def send_message(*args):
    message = entry.get()
    messages_box.config(state='normal')
    messages_box.insert('end', message + '\n')
    messages_box.config(state='disabled')
    entry.delete(0, 'end')

root = tk.Tk()
root.title("Tkinter Chat Box")

messages_frame = tk.Frame(root)
entry = tk.Entry(root, width=50, font=('Arial', 14))
send_button = tk.Button(root, text="Send", command=send_message)

entry.pack(pady=10)
send_button.pack()

messages_box = tk.Text(root, state='disabled', width=50, height=20, font=('Arial', 14))
messages_box.pack()

root.bind('<Return>', send_message)

root.mainloop()
