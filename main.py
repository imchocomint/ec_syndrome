import subprocess
import tkinter
from tkinter import scrolledtext

def cap_command(min_val, max_val):
    result = subprocess.run(
        f"sudo nvidia-smi -lgc {min_val},{max_val}",
        shell=True,
        capture_output=True,
        text=True
    )
    output = result.stdout
    if result.stderr:
        output += ("\n" if output else "") + result.stderr
    if not output.strip():
        output = f"Command finished with return code {result.returncode} (no output)."

    output_window = tkinter.Toplevel(root)
    output_window.title("CLI Output")
    output_window.geometry("400x200")

    text_area = scrolledtext.ScrolledText(output_window, wrap=tkinter.WORD)
    text_area.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)
    text_area.insert(tkinter.END, output)
    text_area.config(state=tkinter.DISABLED)

root = tkinter.Tk()

label = tkinter.Label(root, text="Input min and max GPU clock speeds:")
label.pack(pady=(10, 5))

min_label = tkinter.Label(root, text="Minimum clock speed")
min_label.pack(pady=2)
min_entry = tkinter.Entry(root)
min_entry.pack(pady=2)

max_label = tkinter.Label(root, text="Maximum clock speed")
max_label.pack(pady=2)
max_entry = tkinter.Entry(root)
max_entry.pack(pady=2)

button = tkinter.Button(root, text="Set", width=25, command=lambda: cap_command(min_entry.get(), max_entry.get()))
button.pack(pady=10)

root.geometry("400x320")
root.mainloop()