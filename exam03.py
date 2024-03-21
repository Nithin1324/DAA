import heapq

def prim(graph, start):
    visited = set()
    min_spanning_tree = []
    heap = [(0, start)]

    while heap:
        weight, current_vertex = heapq.heappop(heap)
        if current_vertex not in visited:
            visited.add(current_vertex)
            min_spanning_tree.append((weight, current_vertex))

            for neighbor, neighbor_weight in graph[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_weight, neighbor))

    return min_spanning_tree

def main():
    graph = {}
    num_outposts = int(input("Enter the number of outposts: "))
    for i in range(num_outposts):
        outpost_name = input(f"Enter name of outpost {i+1}: ")
        connections = int(input(f"Enter number of connections for outpost {outpost_name}: "))
        graph[outpost_name] = []
        for _ in range(connections):
            neighbor, weight = input(f"Enter neighbor outpost name and weight for outpost {outpost_name}: ").split()
            graph[outpost_name].append((neighbor, int(weight)))

    start_vertex = input("Enter the starting outpost: ")
    print(prim(graph, start_vertex))

main()
