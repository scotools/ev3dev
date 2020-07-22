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





