import tkinter as tk
from tkinter import filedialog
import logging

root = tk.Tk()

def run_script():
    script_path = filedialog.askopenfilename(title="Select Python file")
    log_path = filedialog.asksaveasfilename(title="Save log file")
    log_level = log_level_var.get()
    
    logging.basicConfig(filename=log_path, level=log_level)
    logging.info(f"Running script: {script_path}")
    
    try:
        exec(open(script_path).read())
        logging.info("Script completed successfully")
    except Exception as e:
        logging.error(f"Script failed with error: {e}")
    
    tk.messagebox.showinfo(title="Script completed", message="Script completed")

log_level_var = tk.StringVar(value="INFO")

tk.Label(root, text="Select Python file:").grid(row=0, column=0)
tk.Button(root, text="Browse", command=run_script).grid(row=0, column=1)

tk.Label(root, text="Log level:").grid(row=1, column=0)
tk.OptionMenu(root, log_level_var, "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").grid(row=1, column=1)

root.mainloop()
