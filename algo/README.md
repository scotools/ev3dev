Make a 2d array, column / row to store the cost

A* algo is a iterative trial with hueristic 
f(n) = g(n) + h(n)

g(n) = the cost to get to the current node
h(n) = the cost from the current node to the end (using a direct path as the lowest cost distance - we don't know the actual path to add)

open-set = the items we are iterating through to find the end
closed-set = the known path

if the open-set is not empty, keep trying to solve, else, no solution

Each cell in the grid contains:
x, y coords
f = 
g = 
h = 

Current is the node in the open-set with the lowest f
var lowestIndex = 0;
for(var i = 0; i < openSet.length; i++) {
  if(openSet[i].f < openSet[
}


Starting coord = 0,0
Goal = 9,9

starting square = 0,0   g(n) = 0 
neigbors are 1,0 and 0,1 are going to have g(n) increase by 1, unless, they are in the closed set!  They have already be choosen as optimal
if(!closedSet.includes(neighbor)) {
  // maybe its in the open set already with a lower score...
  tempG = current.g
  if(openSet.includes(neighbor)) {
    if(tempG < neighbor.g) 
      ;; //do nothing
    else {
      neighbor.g=tempG
      openSet.push(neighbor)
    }
    // now apply the heuristic
    neighbor.h = heuristic(neighbor,end)
    //how long did it take for me to get there, how long to get to the goal added together
    //this is the score of this node we are on
    neighbor.f = neighbor.g + neighbor.h
    // track your pedegry!  
    neighbor.parent = current    
}

if(current == end) {
  done!
}

path = []
var tmp = current
while(tmp.previous) {
  path.push(tmp.previous)
  tmp = tmp.previous
}

path shall contain the optimal path






def heuristic(a,b):
''' Euclidian function, Pythagorean Theorem, what is the shortest distance between 2 points?
A straight line!  Calc the distance between 2 points.'''
  return sqrt((a.x-b.x)*2 + (a.y-b.y)*2)

def manhattan(a,b):
  '''taxi cab algo when you can't move diagonally'''
  return abs(a.x-b.x) + abs(b.x-b.y)


