from ToolBox import graph_from_edges
from ChinesePostmanResult import chinese_postman
from Plot import create_plot


class ButtonMethods:

    def euler_graph_setup(self):
        graph = graph_from_edges('data/graf_eulera.txt')
        path = chinese_postman(graph)
        create_plot(graph, path, 'euler')


    def graph_2odd(self):
        graph = graph_from_edges('data/graf_2odd.txt')
        path = chinese_postman(graph)
        create_plot(graph, path, 'graph_2odd')


    def graph_4odd(self):
        graph = graph_from_edges('data/graf_4odd.txt')
        path = chinese_postman(graph)
        create_plot(graph, path, 'graph_4odd')


    def graph_6odd(self):
        graph = graph_from_edges('data/graf_6odd.txt')
        path = chinese_postman(graph)
        create_plot(graph, path, 'graph_6odd')
