class Node:
    def _init_(self, state, parent, actions):
        self.state = state
        self.parent = parent
        self.actions = actions

def BFS():
    startingNode = input("Enter the initial Node: ")
    destinationNode = input("Enter the Destination Node: ")

    graph = {'Oradea': Node('Oradea', None, ['Zerind' , 'Sibui']),
                  'Zerind': Node('Zerind', None, ['Oradea' , 'Arad']),
                  'Neamt': Node('Neamt', None, ['Iasi']),
                  'Arad': Node('Arad', None, ['Zerind', 'Sibui' , 'Timisoara']),
                  'Isai': Node('Isai', None, ['Neamt','Vaslui']),
                  'Sibui': Node('Sibui', None, ['Oradea', 'Arad' , 'Fagaras' , 'Riminica']),
                  'Fagaras': Node('Fagaras', None, ['Sibui', 'Bucharest']),
                  'Vaslui': Node('Vaslui', None, ['Isai','Urziceni']),
                  'Timisoara': Node('Timisoara', None, ['Arad','Lugoj']),
                  'Riminica': Node('Riminica', None, ['Sibui','Pitesti','Craiova']),
                  'Lugoj': Node('Lugoj', None, ['Timisoara','Mehadia']),
                  'Pitesti': Node('Pitesti', None, ['Riminica','Craiova','Bucharest']),
                  'Mehadia': Node('Mehadia', None, ['Lugoj','Drobeta']),
                  'Bucharest': Node('Bucharest', None, ['Fagaras','Pitesti','Urziceni']),
                  'Urziceni': Node('Urziceni', None, ['Bucharest','Hirsova','Vaslui']),
                  'Hirsova': Node('Hirsova', None, ['Urziceni','Eforie']),
                  'Drobeta': Node('Drobeta', None, ['Mehndia','Craiova']),
                  'Craiova': Node('Craiova', None, ['Drobeta','Riminica','Pitesti']),
                  'Giurgui': Node('Giurgui', None, ['Bucharest']),
                  'Eforie': Node('Eforie', None, ['Hirsova'])}
    queue = [startingNode]
    visited = []
    
    while len(queue) != 0:
        temp = queue.pop(0)
        visited.append(temp)
        
        for child in graph[temp].actions:
            if child not in queue and child not in visited:
                graph[child].parent = temp
                if graph[child].state == destinationNode:
                    return roadMap(graph, startingNode ,destinationNode)
                queue.append(child)
                
def roadMap(graph, startingNode, destinationNode):
    temporary = [destinationNode]
    parentCurrent = graph[destinationNode].parent
    
    while parentCurrent != None:
        temporary.append(parentCurrent)
        parentCurrent = graph[parentCurrent].parent
    temporary.reverse()
    return temporary

sol = BFS()
print()
print("Shortest Path Is: " , sol)


def solveMazeso(maze):
    R, C = len(maze), len(maze[0])

    start = (0, 0)
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        else:
            continue
        break
    else:
        return None

    queue = deque()
    queue.appendleft((start[0], start[1], 0, [start[0] * C + start[1]]))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        if maze[coord[0]][coord[1]] == "E":
            return coord[2], [[i//C, i%C] for i in coord[3]] # Return path length, boxes on path

        for dir in directions:
            nr, nc = coord[0] + dir[0], coord[1] + dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]): continue
            queue.appendleft((nr, nc, coord[2] + 1, coord[3] + [nr * C + nc]))
