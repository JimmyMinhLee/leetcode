graph = [[1, 2], [3], [3], []]

def solution(graph):
    zero = graph[0]
    initial_path = [0]
    ans = []
    for neighbor in zero:
        dfs(ans, graph, neighbor, initial_path + [neighbor])
    return ans

def dfs(ans, graph, node, path):
    neighbors = graph[node]
    if len(neighbors) == 0:
        ans.append(path)
    for neighbor in neighbors:
        dfs(ans, graph, neighbor, path+[neighbor])
    return 

graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(solution(graph))
