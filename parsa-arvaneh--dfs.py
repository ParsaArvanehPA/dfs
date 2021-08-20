##
# By Parsa Arvaneh
# پارسا اروانه
##
##
##
##

from collections import defaultdict
class DfsGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.isFound = False

    def create_wings(self, u, v):
        self.graph[u].append(v)

    def graph_iterator(self, node, visited):
        visited.add(node)
        print(f'step {len(visited)}: \t{visited}')

        for graph_cell in self.graph[node]:
            if graph_cell not in visited:
                self.graph_iterator(graph_cell, visited)

    def full_dfs_iteration(self, start_node):
        visited = set()
        self.graph_iterator(start_node, visited)

    def node_iterator(self, node, desired_node, visited):
        if not self.isFound:
            visited.add(node)
            print(node, end=' ')
            if node is desired_node:
                self.isFound = True

            for graph_cell in self.graph[node]:
                if graph_cell not in visited:
                    self.node_iterator(graph_cell, desired_node, visited)

    def node_finder(self, start_node, desired_node):
        visited = set()
        self.node_iterator(start_node, desired_node, visited)
        if not self.isFound:
            print(f'\n\n{">"*20}\tNO SUCH NODE IN THIS GRAPH!\t{"<"*20}')


# اینجا باید خونه های گراف خودتون رو بسازید
graph = DfsGraph()
graph.create_wings(1, 2)
graph.create_wings(1, 3)
graph.create_wings(1, 4)
graph.create_wings(2, 5)
graph.create_wings(2, 6)
graph.create_wings(3, 7)
graph.create_wings(4, 8)
graph.create_wings(4, 9)
graph.create_wings(5, 10)
graph.create_wings(6, 11)
graph.create_wings(6, 12)
graph.create_wings(6, 13)
graph.create_wings(7, 14)
graph.create_wings(7, 15)
graph.create_wings(8, 16)
graph.create_wings(13, 17)
graph.create_wings(13, 18)
graph.create_wings(16, 19)
graph.create_wings(16, 20)

# برای پیمایش کامل درخت
print(f'{"="*70}\tFULL ITERATION\t{"="*70}')
graph.full_dfs_iteration(1)

# برای پیدا کردن خونه مشخصی از گراف
# اولین مقدرار، خونه شروع است
# مقدار دوم، خونه ای که دنبالش هستید
# graph.node_finder(start_node, desired_node)
print(f'\n{"="*70}\tFINDING SPECIFIC NODE\t{"="*70}')
graph.node_finder(1, 7)
