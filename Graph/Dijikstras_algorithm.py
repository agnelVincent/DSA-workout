import heapq

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []
}

def dijikstra(graph , start):

    distances = {node : float('inf') for node in graph}
    distances[start] = 0

    pq = [(0 , start)]

    while pq:
        current_dist , node = heapq.heappop(pq)

        if current_dist > distances[node]:
            continue

        for neighbor , weight in graph[node]:
            dist = current_dist + weight
            
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq , (dist , neighbor))

    return distances

print(graph)
print(dijikstra(graph , 'A'))