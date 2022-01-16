import os
from ToolBox import graph_from_edges
from ChinesePostmanResult import chinese_postman
from Plot import create_plot
from tkinter.filedialog import askopenfilename


def resolve_graph(input_path, name):
    graph = graph_from_edges(input_path)
    path, to_connect = chinese_postman(graph)
    create_plot(graph, path, name, to_connect)


def move_files(window):
    files = os.listdir()
    for file in files:
        if file[-5:] == '.html':
            os.replace(file, f'output/{file}')
    window.destroy()


def ask_for_input():
    filetypes = (
        ('PDF files', '*.txt'),
        ('All files', '*.*')
    )
    input_graph = askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    name = os.path.basename(input_graph)
    name = os.path.splitext(name)[0]
    resolve_graph(input_graph, name)
