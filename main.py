import tkinter as tk
from GUI import ButtonMethods


if __name__ == '__main__':
    # Create window
    window = tk.Tk()
    window.title('Problem chińskiego listonosza')

    # Create class that will control source scripts
    BT = ButtonMethods()

    instruction_text = "Wybierz graf do narysowania lub wprowadź własny graf"
    instruction = tk.Label(text=instruction_text, width=50, height=5)
    instruction.pack()

    button_euler = tk.Button(text="Graf Eulera", width=25, height=5)
    button_euler.bind("<Button-1>", lambda e: BT.euler_graph_setup())
    button_euler.pack()

    button_2odd = tk.Button(text="Graf z dwoma wierzchołkami\no " +
                                 "nieparzystych stopniach", width=25, height=5)
    button_2odd.bind("<Button-1>", lambda e: BT.graph_2odd())
    button_2odd.pack()

    button_4odd = tk.Button(text="Graf z czterema wierzchołkami\no " +
                                 "nieparzystych stopniach", width=25, height=5)
    button_4odd.bind("<Button-1>", lambda e: BT.graph_4odd())
    button_4odd.pack()

    button_6odd = tk.Button(text="Graf z sześcioma wierzchołkami\no " +
                                 "nieparzystych stopniach", width=25, height=5)
    button_6odd.bind("<Button-1>", lambda e: BT.graph_6odd())
    button_6odd.pack()


    window.mainloop()