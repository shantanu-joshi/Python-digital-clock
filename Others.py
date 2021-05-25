import tkinter as tk

def do_something(phrase):
    return phrase + phrase

def main():
    root = tk.Tk()
    root.title("Demo")

    tk.Label(root, text="Please enter a sentence: ").grid(row=0)
    user_input = tk.Entry(root)
    user_input.grid(row=0, column=1)
    result = tk.Label(root, text='')
    result.grid(row=2, column=0, columnspan=2)
    btn = tk.Button(root, text='Do something')
    btn.config(command=lambda: result.config(text=do_something(user_input.get())))
    btn.grid(row=1, column=1, sticky=tk.W, pady=4)

    root.mainloop()

if __name__ == "__main__":
    main()