def BFS();
initialState = 'D'
goalState = 'F'
graph = {'A': Node('A', None, ['B', 'C', 'E'],None),
         'B': Node('B', None, ['A', 'D', 'E'],None),
         'C': Node('C', None, ['A', 'F', 'G'],None),
         'D': Node('D', None, ['B', 'E'],None),
         'E': Node('E', None, ['A', 'B', 'D'],None),
         'F': Node('F', None, ['C'],None),
         'G': Node('G', None, ['C'],None)}
frontier = [initialState]
explored=[]
while len(frontier)!=0;
currentNode = frontier.pop(0)
explpored.append(currentNode)
for child in graph[currentNode].actions:
    if child not in frontier and child not in explored:
        graph[child].parent=currentNode
        if graph[child].state==goalState:
            return actionSequence(graph, initialState, goalState)
        frontier.append(child)
        solution = BFS()
        print(solution)
