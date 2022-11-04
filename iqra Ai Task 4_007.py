
# Imagine going from Arad to Bucharest in the following map.??
# Implement by Depth First Search ....??

class Node:
  def _init_(self, state, parent, actions, totalCost):
    self.state = state
    self.parent = parent
    self.actions = actions
    self.totalCost = totalCost
  
def DFS():
  initialState = input("Enter initial Node: ")
  destinationState = input("Enter destination Node: ")

  graph = {'Oradea': Node('Oradea', None, ['Zerind' , 'Sibui'], None),
                  'Zerind': Node('Zerind', None, ['Oradea' , 'Arad'], None),
                  'Neamt': Node('Neamt', None, ['Iasi'], None),
                  'Arad': Node('Arad', None, ['Zerind', 'Sibui' , 'Timisoara'], None),
                  'Isai': Node('Isai', None, ['Neamt','Vaslui'], None),
                  'Sibui': Node('Sibui', None, ['Oradea', 'Arad' , 'Fagaras'], None),
                  'Fagaras': Node('Fagaras', None, ['Sibui', 'Bucharest'], None),
                  'Vaslui': Node('Vaslui', None, ['Isai','Urziceni'], None),
                  'Timisoara': Node('Timisoara', None, ['Arad','Lugoj'], None),
                  'Riminica': Node('Riminica', None, ['Sibui','Pitesti','Craiova'], None),
                  'Lugoj': Node('Lugoj', None, ['Timisoara','Mehadia'], None),
                  'Pitesti': Node('Pitesti', None, ['Riminica','Craiova','Bucharest'], None),
                  'Mehadia': Node('Mehadia', None, ['Lugoj','Drobeta'], None),
                  'Bucharest': Node('Bucharest', None, ['Fagaras','Pitesti','Urziceni'], None),
                  'Urziceni': Node('Urziceni', None, ['Bucharest','Hirsova','Vaslui'], None),
                  'Hirsova': Node('Hirsova', None, ['Urziceni','Eforie'], None),
                  'Drobeta': Node('Drobeta', None, ['Mehadia','Craiova'], None),
                  'Craiova': Node('Craiova', None, ['Drobeta','Riminica','Pitesti'], None),
                  'Giurgui': Node('Giurgui', None, ['Bucharest'], None),
                  'Eforie': Node('Eforie', None, ['Hirsova'], None)}

  frontierList = [initialState]
  visitedList = []

  while len(frontierList) != 0:
    currentNode = frontierList.pop(len(frontierList)-1)
    visitedList.append(currentNode)
    currentChildren = 0
    for child in graph[currentNode].actions:
      if child not in frontierList and child not in visitedList:
        graph[child].parent = currentNode
        if graph[child].state == destinationState:
          print("Explored Nodes are: ", visitedList)
          return roadMap(graph, initialState, destinationState)
        currentChildren = currentChildren + 1
        frontierList.append(child)
    if currentChildren == 0:
      del visitedList[len(visitedList)-1]

def roadMap(graph, initialState, destinationState):
  solution = [destinationState]
  currentParent = graph[destinationState].parent

  while currentParent != None:
    solution.append(currentParent)
    currentParent = graph[currentParent].parent
  solution.reverse()
  return solution

sol = DFS()
print(sol)
Enter initial Node: Arad
Enter destination Node: Bucharest
Explored Nodes are:  ['Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti']
['Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest']


 A class to store a Trie node
class Trie:
    # Constructor
    def _init_(self):
        self.character = {}
        self.isLeaf = False  # true when the node is a leaf node
 
 
# Iterative function to insert a string into a Trie
def insert(root, s):
    # start from the root node
    curr = root
 
    for ch in s:
        # go to the next node (create if the path doesn't exist)
        curr = curr.character.setdefault(ch, Trie())
 
    curr.isLeaf = True
 
 
# Below lists detail all eight possible movements from a cell
# (top, right, bottom, left, and four diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
 
# The function returns false if (x, y) is not valid matrix coordinates
# or cell (x, y) is already processed or doesn't lead to the solution
def isSafe(x, y, processed, board, ch):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0])) and \
           not processed[x][y] and (board[x][y] == ch)
 
 
# A recursive function to search valid words present in a boggle using trie
def searchBoggle(root, board, i, j, processed, path, result):
    # if a leaf node is encountered
    if root.isLeaf:
        # update result with the current word
        result.add(path)
 
    # mark the current cell as processed
    processed[i][j] = True
 
    # traverse all children of the current Trie node
    for key, value in root.character.items():
 
        # check for all eight possible movements from the current cell
        for k in range(len(row)):
 
            # skip if a cell is invalid, or it is already processed
            # or doesn't lead to any path in the Trie
            if isSafe(i + row[k], j + col[k], processed, board, key):
                searchBoggle(value, board, i + row[k], j + col[k],
                             processed, path + key, result)
 
    # backtrack: mark the current cell as unprocessed
    processed[i][j] = False
 
 
# Function to search for a given set of words in a boggle
def searchInBoggle(board, words):
    # construct a set for storing the result
    result = set()
 
    # base case
    if not board or not len(board):
        return
 
    # insert all words into a trie
    root = Trie()
    for word in words:
        insert(root, word)
 
    # `M × N` board
    (M, N) = (len(board), len(board[0]))
 
    # construct a matrix to store whether a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]
 
    # consider each character in the matrix
    for i in range(M):
        for j in range(N):
            ch = board[i][j]  # current character
 
            # proceed only if the current character is a child of the Trie root node
            if ch in root.character:
                searchBoggle(root.character[ch], board, i, j, processed, ch, result)
 
    # return the result set
    return result
 
 

# Board
board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
  ]

# Words
words = ['START', 'NOTE', 'SAND', 'STONED']
searchInBoggle(board, words)

validWords = searchInBoggle(board, words)
print(validWords)
{'STONED', 'NOTE', 'SAND'}
# Lab Activity 01
# Depth First Serch
# Initial State is 'D' and Destination State is 'C'

class Node:
  def _init_(self, state, parent, actions, totalCost):
    self.state = state
    self.parent = parent
    self.actions = actions
    self.totalCost = totalCost

def DepthFirstSearch():
  initialState = 'D'
  goalState = 'C'

  graph = {'A': Node('A', None, ['B', 'E', 'C'], None),
           'B': Node('B', None, ['D', 'E', 'A'], None),
           'C': Node('C', None, ['A', 'F', 'G'], None),
           'D': Node('D', None, ['B', 'E'], None),
           'E': Node('E', None, ['A', 'B', 'D'], None),
           'F': Node('F', None, ['C'], None),
           'G': Node('G', None, ['C'], None)}
  
  frontierList = [initialState]
  visitedList = []

  while len(frontierList) != 0:
    currentNode = frontierList.pop(len(frontierList)-1)
    visitedList.append(currentNode)
    currentChildren = 0
    for child in graph[currentNode].actions:
      if child not in frontierList and child not in visitedList:
        graph[child].parent = currentNode
        if graph[child].state == goalState:
          print("Visited Nodes are: ", visitedList)
          return roadMap(graph, initialState, goalState)
        currentChildren = currentChildren + 1
        frontierList.append(child)
    if currentChildren == 0:
      del visitedList[len(visitedList)-1]

def roadMap(graph, initialState, goalState):
  solutionList = [goalState]
  currentParent = graph[goalState].parent

  while currentParent != None:
    solutionList.append(currentParent)
    currentParent = graph[currentParent].parent
  solutionList.reverse()
  return solutionList

sol = DepthFirstSearch()
print(sol)
Visited Nodes are:  ['D', 'E', 'A']
['D', 'E', 'A', 'C']
# Lab Activity 02
# Depth First Serch


class Node:
  def  _init_(self,state,parent,actions,totalcast):
    self.state=state 
    self.parent=parent
    self.actions=actions
    self.totalcast=totalcast
def DFS():
  ist='A' 
  goalstate='D'
    #lets take a graph 
  graph={'A':Node('A',None,['B','E','C'],None),
        'B':Node('B',None,['D','E','A'],None), 
        'C':Node('C',None,['A','F','G'],None),
        'D':Node('D',None,['B','E'],None),
        'E':Node('E',None,['A','B','D'],None),
        'F':Node('F',None,['C'],None),
        'G':Node('G',None,['C'],None)}
  front=[ist]
  explored=[]
  while len(front)!=0:
    currentnode=front.pop(len(front)-1)
    print(currentnode)
    explored.append(currentnode)
    currentchildren=0
    for child in graph [currentnode].actions:
         if child   not in front and child  not in explored:
             graph[child].parent=currentnode
             if graph [child].state==goalstate:
                 print(explored)
                 return actionsequence (graph,ist,goalstate)
             currentchildren=currentchildren+1
             front.append(child)
    if currentchildren==0:
          del explored[len(explored)-1]
    
def actionsequence(graph,ist,goalstate):

            solution=[goalstate]
            currentparent=graph[goalstate].parent
            while currentparent !=None:
              solution.append(currentparent)
              currentparent=graph[currentparent].parent
            solution.reverse()
            return solution

solution = DFS()
print(solution)
A
C
G
F
E
['A', 'C', 'E']
['A', 'E', 'D']
