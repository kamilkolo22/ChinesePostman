from ToolBox import *


if __name__ == '__main__':
    tree = {}
    add_edge(tree, (1, 2))
    add_edge(tree, (2, 3))
    add_edge(tree, (1, 3))
    add_edge(tree, (3, 4))
    add_edge(tree, (4, 5))
    add_edge(tree, (3, 5))

    print(check_euler(tree))
    print(dfs_euler(tree, 1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
