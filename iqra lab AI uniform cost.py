{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5bb35864",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shortest path is: ['C', 'F', 'E', 'B']\n"
     ]
    }
   ],
   "source": [
    "# ------------------------- USAMA MANSOOR-------FA20-BCS-026----------------#\n",
    "#-----------ARTIFICIAL INTELLIGENCE---------------#\n",
    "#-------UNIFORM COST SEARCH------------#\n",
    "import math\n",
    "\n",
    "class Node:\n",
    "    def __init__(self, state, parent, actions, totalCost):\n",
    "        self.state = state\n",
    "        self.parent = parent\n",
    "        self.actions = actions\n",
    "        self.totalCost = totalCost\n",
    "        \n",
    "\n",
    "def FindMin(frontier):\n",
    "    minValue = math.inf\n",
    "    node = ''\n",
    "    for i in frontier:\n",
    "        if minValue > frontier[i][1]:\n",
    "            minValue = frontier[i][1]\n",
    "            node = i\n",
    "    return node\n",
    "\n",
    "def actionSequence(graph, initialState, goalState):\n",
    "    solution = [goalState]\n",
    "    currentParent = graph[goalState].parent\n",
    "    while currentParent != None:\n",
    "        solution.append(currentParent)\n",
    "        currentParent = graph[currentParent].parent\n",
    "    solution.reverse()\n",
    "    return solution\n",
    "\n",
    "\n",
    "def UCS():\n",
    "    initialState = 'C'\n",
    "    goalState = 'B'\n",
    "    \n",
    "    graph = {'A': Node('A', None, [('B',6), ('C',9), ('E',1)], 0),\n",
    "             'B': Node('B', None, [('A',6), ('D',3), ('E',4)], 0),\n",
    "             'C': Node('C', None, [('A',9), ('F',2), ('G',3)], 0),\n",
    "             'D': Node('D', None, [('B',3), ('E',5), ('F',7)], 0),\n",
    "             'E': Node('E', None, [('A',1), ('B',4), ('D',5), ('F',6)], 0),\n",
    "             'F': Node('F', None, [('C',2), ('E',6), ('D',7)], 0),\n",
    "             'G': Node('G', None, [('C',3)], 0)}\n",
    "    frontier = dict()\n",
    "    frontier[initialState] = (None, 0)\n",
    "    explored = []\n",
    "    \n",
    "    while len(frontier) != 0:\n",
    "        currentNode = FindMin(frontier)\n",
    "        del frontier[currentNode]\n",
    "        if graph[currentNode].state == goalState:\n",
    "            return actionSequence(graph, initialState, goalState)\n",
    "        explored.append(currentNode)\n",
    "        \n",
    "        for child in graph[currentNode].actions:\n",
    "            currentCost = child[1] + graph[currentNode].totalCost\n",
    "            if child[0] not in frontier and child[0] not in explored:\n",
    "                graph[child[0]].parent = currentNode\n",
    "                graph[child[0]].totalCost = currentCost\n",
    "                frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)\n",
    "            elif child[0] in frontier:\n",
    "                if frontier[child[0]][1] < currentCost:\n",
    "                    graph[child[0]].parent = frontier[child[0]][0]\n",
    "                    graph[child[0]].totalCost = frontier[child[0]][1]\n",
    "                else:\n",
    "                    frontier[child[0]] = (currentNode, currentCost)\n",
    "                    graph[child[0]].totalCost = frontier[child[0]][1]\n",
    "                    \n",
    "sol = UCS()\n",
    "print(f\"Shortest path is: {sol}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
