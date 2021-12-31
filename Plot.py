from pyvis.network import Network
var_options = """
var options = {
  "nodes": {
    "physics": false,
    "size": 10
  },
  "edges": {
    "color": {
      "color": "rgba(0,255,0,1)", 
      "inherit": false
    },
    "smooth": false
  },
  "physics": {
    "minVelocity": 0.75
  }
}
"""


def create_plot(graph, path, name, to_connect):
    if len(to_connect):
        title = 'Dodano sciezki miedzy: '
        for pair in to_connect:
            title += f'{pair[0]} i {pair[1]}, '
        net = Network(height='1000px', width='1000px', heading=title)
    else:
        net = Network(height='1000px', width='1000px')

    for v in graph:
        add_node(graph, net, v)
        for u in graph[v]:
            if not u[0] in net.get_nodes():
                add_node(graph, net, u[0])
            net.add_edge(v, u[0], label=u[1])
    for i in range(len(path)):
        net.get_node(path[i])['label'] += f' ({i+1})'
    net.set_options(var_options)
    net.show(f'{name}.html')


def add_node(graph, net, v):
    if len(graph[v]) % 2:
        net.add_node(v, v, title=v, color='red')
    else:
        net.add_node(v, v, title=v, color='blue')
