graph = {'A': Node('A', None, [('B',6),  ('C',9),  ('E',1)], 0),
         'B': Node('B', None, [('A',6),  ('D',3),  ('E',4)], 0),
         'C': Node('C', None, [('A',9),  ('F',2),  ('G',3)], 0),
         'D': Node('D', None, [('B',3),  ('E',5),  ('F',7)], 0),
         'E': Node('E', None, [('A',1),  ('B',4),  ('D',5)],  ('F',6), 0),
         'F': Node('F', None, [('C',2),  ('E',6),  ('D',7)], 0),
         'G': Node('G', None, [('C',3)], 0)}
import math

def findMin(frontier):
    #returns that node in the frontier which has a lowest cost
    minV=math.inf
    node=''
    for i in frontier
