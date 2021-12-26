from pyvis.network import Network
import pandas as pd

# got_net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
#
# # set the physics layout of the network
# got_net.barnes_hut()
# got_data = pd.read_csv('https://www.macalester.edu/~abeverid/data/stormofswords.csv')
#
# sources = got_data['Source']
# targets = got_data['Target']
# weights = got_data['Weight']
#
# edge_data = zip(sources, targets, weights)
#
# for e in edge_data:
#     src = e[0]
#     dst = e[1]
#     w = e[2]
#
#     got_net.add_node(src, src, title=src)
#     got_net.add_node(dst, dst, title=dst)
#     got_net.add_edge(src, dst, value=w)
#
# neighbor_map = got_net.get_adj_list()
#
# # add neighbor data to node hover data
# for node in got_net.nodes:
#     node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
#     node['value'] = len(neighbor_map[node['id']])
#
# got_net.show_buttons()
# got_net.show('gameofthrones.html')

def create_plot(graph, path, name):
    net = Network()
    for v in graph:
        add_node(graph, net, v)
        for u in graph[v]:
            if not u[0] in net.get_nodes():
                add_node(graph, net, u[0])
            net.add_edge(v, u[0], label=u[1])
    for i in range(len(path)):
        net.get_node(path[i])['label'] += f' ({i+1})'
    net.show_buttons() # TODO comment this after app release
    net.show(f'{name}.html')


def add_node(graph, net, v):
    if len(graph[v]) % 2:
        net.add_node(v, v, title=v, color='red')
    else:
        net.add_node(v, v, title=v, color='blue')
