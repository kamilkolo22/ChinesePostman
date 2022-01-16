import tkinter as tk
from GUI import *


if __name__ == '__main__':
    # Create window
    window = tk.Tk()
    window.title('Problem chińskiego listonosza')

    instruction_text = "Wybierz graf do narysowania lub wprowadź własny graf"
    instruction = tk.Label(text=instruction_text, width=50, height=5)
    instruction.pack()

    button_euler = tk.Button(text="Graf Eulera", width=25, height=5)
    button_euler.bind("<Button-1>",
                      lambda e: resolve_graph('data/graf_eulera.txt', 'euler'))
    button_euler.pack()

    button_2odd = tk.Button(text="Graf z dwoma wierzchołkami\no " +
                                 "nieparzystych stopniach", width=25, height=5)
    button_2odd.bind("<Button-1>",
                     lambda e: resolve_graph('data/graf_2odd.txt', 'graf_2odd'))
    button_2odd.pack()

    button_4odd = tk.Button(text="Graf z czterema wierzchołkami\no " +
                                 "nieparzystych stopniach", width=25, height=5)
    button_4odd.bind("<Button-1>",
                     lambda e: resolve_graph('data/graf_4odd.txt', 'graf_4odd'))
    button_4odd.pack()

    button_6odd = tk.Button(text="Graf z sześcioma wierzchołkami\no " +
                                 "nieparzystych stopniach", width=25, height=5)
    button_6odd.bind("<Button-1>",
                     lambda e: resolve_graph('data/graf_6odd.txt', 'graf_6odd'))
    button_6odd.pack()

    button_newgraph = tk.Button(text='Wybierz graf w postaci\n listy ' +
                                     'sąsiedstwa z pliku', width=25, height=5)
    button_newgraph.bind("<Button-1>", lambda e: ask_for_input())
    button_newgraph.pack()

    window.protocol("WM_DELETE_WINDOW", lambda: move_files(window))
    window.mainloop()
