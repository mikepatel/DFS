"""
https://leetcode.com/problems/all-paths-from-source-to-target/
"""


################################################################################
# DFS
def dfs(visited, graph, node):
    if node == n - 1:
        visited[node] = True
        paths.append(list(visited.keys()))
        return

    if node not in visited:
        visited[node] = True
        for adjacent_node in graph[node]:
            dfs(visited, graph, adjacent_node)
            visited.pop(adjacent_node)  # new dfs path


################################################################################
# Main
if __name__ == "__main__":
    # inputs
    graph = [[1, 2], [3], [3], []]

    # restructure graph
    temp = {}
    for i in range(len(graph)):
        temp[i] = graph[i]

    graph = temp

    # driver code
    paths = []
    visited = {}
    n = len(graph)
    dfs(visited, graph, node=0)  # all paths start from node 0

    print(f'All paths from node 0 to node {n-1}: {paths}')
