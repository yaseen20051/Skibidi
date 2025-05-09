from collections import deque



def constructadj(V, edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    return adj



def topologicalSort(V, edges):
    adj = constructadj(V, edges)
    indegree = [0] * V


    for u in range(V):
        for v in adj[u]:
            indegree[v] += 1


    q = deque([i for i in range(V) if indegree[i] == 0])

    result = []
    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")
        return []

    return result


if __name__ == "__main__":
    V = 8
    edges = [[7, 5], [7, 6], [6, 4], [6, 3], [5, 4], [5, 2],[4,1],[2,1],[3,1],[1,0]]
    result = topologicalSort(V, edges)
    if result:
        print("Topological Order:", result)