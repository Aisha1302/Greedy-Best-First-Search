
import heapq
def greedySearch(graph, start, goal, heuristic):
    queue = []
    heapq.heappush(queue, (heuristic[start], start))

    # track visited nodes
    visited = set()

    # track the path
    path = {start: None}

    while queue:
        current_cost, current_node = heapq.heappop(queue)
        if current_node == goal:
            return reconstruct_path(path, start, goal)

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                path[neighbor] = current_node
                heapq.heappush(queue, (heuristic[neighbor], neighbor))
                visited.add(neighbor)

    return None

def reconstruct_path(path, start, goal):
    current = goal
    path_list = []
    while current is not None:
        path_list.append(current)
        current = path[current]
    path_list.reverse()
    return path_list


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'
path = greedySearch(graph, start, goal, heuristic)

print("Path from start to goal:", path)


