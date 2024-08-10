import os
import sys
import shutil
import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser
def list_files():
    files = "\n".join(os.listdir('.'))
    output_text.insert(tk.END, f"{os.getcwd()} >>> ls\n{files}\n\n", "command")
def change_directory(path):
    try:
        os.chdir(path)
        output_text.insert(tk.END, f"{os.getcwd()} >>> cd {path}\nChanged directory to {os.getcwd()}\n\n", "command")
    except Exception as e:
        output_text.insert(tk.END, f"{os.getcwd()} >>> cd {path}\nError: {e}\n\n", "error")
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            output_text.insert(tk.END, f"{os.getcwd()} >>> cat {filename}\n" + file.read() + "\n\n", "command")
    except Exception as e:
        output_text.insert(tk.END, f"{os.getcwd()} >>> cat {filename}\nError: {e}\n\n", "error")
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write('')
        output_text.insert(tk.END, f"{os.getcwd()} >>> touch {filename}\nFile '{filename}' created.\n\n", "command")
    except Exception as e:
        output_text.insert(tk.END, f"{os.getcwd()} >>> touch {filename}\nError: {e}\n\n", "error")
def delete_file(filename):
    if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{filename}'?"):
        try:
            os.remove(filename)
            output_text.insert(tk.END, f"{os.getcwd()} >>> rm {filename}\nFile '{filename}' deleted.\n\n", "command")
        except Exception as e:
            output_text.insert(tk.END, f"{os.getcwd()} >>> rm {filename}\nError: {e}\n\n", "error")
    else:
        output_text.insert(tk.END, f"{os.getcwd()} >>> rm {filename}\nDelete cancelled.\n\n", "command")
def create_directory(dirname):
    try:
        os.mkdir(dirname)
        output_text.insert(tk.END, f"{os.getcwd()} >>> mkdir {dirname}\nDirectory '{dirname}' created.\n\n", "command")
    except Exception as e:
        output_text.insert(tk.END, f"{os.getcwd()} >>> mkdir {dirname}\nError: {e}\n\n", "error")
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        output_text.insert(tk.END, f"{os.getcwd()} >>> cp {src} {dest}\nFile '{src}' copied to '{dest}'.\n\n", "command")
    except Exception as e:
        output_text.insert(tk.END, f"{os.getcwd()} >>> cp {src} {dest}\nError: {e}\n\n", "error")
def shutdown(now=False):
    if now:
        output_text.insert(tk.END, f"{os.getcwd()} >>> shutdown --now\nShutting down immediately...\n\n", "command")
        root.quit()
        os.system("shutdown -s -f -t 0")
    else:
        output_text.insert(tk.END, f"{os.getcwd()} >>> shutdown\nShutting down...\n\n", "command")
        root.quit()
        os.system("shutdown -s")
def open_browser(url):
    try:
        webbrowser.open(url)
        output_text.insert(tk.END, f"{os.getcwd()} >>> open {url}\nOpening {url} in browser...\n\n", "command")
    except Exception as e:
        output_text.insert(tk.END, f"{os.getcwd()} >>> open {url}\nError: {e}\n\n", "error")
def clear_command():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Welcome to Simple Python OS! Type 'help' to see available commands.\n\n")
def python():
    pythontext = """
 ######   ##  ##   ######   ##   ##   #####   ##   ##
  ##  ##  ##  ##   # ## #   ##   ##  ##   ##  ###  ##
  ##  ##  ##  ##     ##     ##   ##  ##   ##  #### ##
  #####    ####      ##     #######  ##   ##  ## ####
  ##        ##       ##     ##   ##  ##   ##  ##  ###
  ##        ##       ##     ##   ##  ##   ##  ##   ##
 ####      ####     ####    ##   ##   #####   ##   ##

"""
    output_text.insert(tk.END,pythontext)
def show_help():
    help_text = """
Available commands:
ls               - List files in the current directory
cd <path>        - Change directory
cat <filename>   - Display file content
touch <filename> - Create a new file
rm <filename>    - Delete a file
mkdir <dirname>  - Create a new directory
cp <src> <dest>  - Copy a file
openurl <url>    - Open URL in web browser
shutdown [--now] - Shutdown the system
help             - Show this help message
exit             - Exit the program
clear            - Clear the commandline
"""
    output_text.insert(tk.END, f"{os.getcwd()} >>> help\n{help_text}\n\n", "command")
def execute_command(event=None):
    command = entry.get().strip().split()
    entry.delete(0, tk.END)
    if not command:
        return
    cmd = command[0].lower()
    options = command[1:]
    if cmd == 'exit':
        output_text.insert(tk.END, f"{os.getcwd()} >>> exit\nExiting...\n\n", "command")
        root.quit()
    elif cmd == 'ls':
        list_files()
    elif cmd == 'cd':
        if options:
            change_directory(options[0])
        else:
            output_text.insert(tk.END, f"{os.getcwd()} >>> cd\nUsage: cd <path>\n\n", "error")
    elif cmd == 'cat':
        if options:
            read_file(options[0])
        else:
            output_text.insert(tk.END, f"{os.getcwd()} >>> cat\nUsage: cat <filename>\n\n", "error")
    elif cmd == 'touch':
        if options:
            create_file(options[0])
        else:
            output_text.insert(tk.END, f"{os.getcwd()} >>> touch\nUsage: touch <filename>\n\n", "error")
    elif cmd == 'rm':
        if options:
            delete_file(options[0])
        else:
            output_text.insert(tk.END, f"{os.getcwd()} >>> rm\nUsage: rm <filename>\n\n", "error")
    elif cmd == 'mkdir':
        if options:
            create_directory(options[0])
        else:
            output_text.insert(tk.END, f"{os.getcwd()} >>> mkdir\nUsage: mkdir <dirname>\n\n", "error")
    elif cmd == 'cp':
        if len(options) > 1:
            copy_file(options[0], options[1])
        else:
            output_text.insert(tk.END, f"{os.getcwd()} >>> cp\nUsage: cp <src> <dest>\n\n", "error")
    elif cmd == 'openurl':
        if options:
            open_browser(options[0])
        else:
            output_text.insert(tk.END, f"{os.getcwd()} >>> open\nUsage: open <url>\n\n", "error")
    elif cmd == 'shutdown':
        if '--now' in options:
            shutdown(now=True)
        else:
            shutdown()
    elif cmd == 'help':
        show_help()
    elif cmd == 'clear':
        clear_command()
    elif cmd == 'python':
        python()
    else:
        output_text.insert(tk.END, f"{os.getcwd()} >>> {cmd}\nUnknown command: {cmd}\n\n", "error")
root = tk.Tk()
root.title("Simple Python OS")
root.geometry("600x400")
root.resizable(False, False)
frame = tk.Frame(root)
frame.pack(pady=10)
entry = tk.Entry(frame, width=70)
entry.pack(side=tk.LEFT, padx=10)
entry.bind("<Return>", execute_command)
execute_button = tk.Button(frame, text="Execute", command=execute_command)
execute_button.pack(side=tk.LEFT)
output_text = scrolledtext.ScrolledText(root, width=80, height=20, fg = "black",wrap=tk.WORD, bg='white',insertbackground='black')
output_text.pack(pady=10)
output_text.insert(tk.END, "Welcome to Simple Python OS! Type 'help' to see available commands.\n\n")
output_text.insert(tk.END, f"{os.getcwd()} >>>\n\n")
output_text.tag_config('command', foreground='black')
output_text.tag_config('error', foreground='red')
root.mainloop()
