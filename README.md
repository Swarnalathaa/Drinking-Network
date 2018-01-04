# Drinking-Network


I have implemented Drinking Network system as graph. Node in the network is represented by the graph's node/vertices and all pipes and valves of the network represnt the edges.

Each node has a name and the pipe and valve connecting the nodes has a Pipe ID and Valve ID respectively. We are provided with excel sheets with sheet1) contains pipe ID and there corresponding connecting node and sheet2)contains pipe ID and there corresponding connecting node. The example of the sheet in shown below:

----------------------------------                                     
PIPE ID |   NODE 1   |  NODE 2
--------|------------|------------
pipe 1  |  node35    |  node54
pipe 45 |  node5     |  node789
  .     |    .       |    .
  .     |    .       |    .
  .     |    .       |    .
  .     |    .       |    .
  
  
-----------------------------------
VALVE ID |   NODE 1   |  NODE 2
---------|------------|------------
valve1   |  node3     |  node54
valve143 |  node92    |  node79
  .      |    .       |    .
  .      |    .       |    .
  .      |    .       |    .
  .      |    .       |    .
  
  
All valves are pipes but only additional option is that it can be closed or opened as per our requirement. 
  
Problem statement : We have to write an algorithm such when the Pipe ID is given as the input to the algorithm it should print all the valves ID's that has to be closed.

Solution : I have used DFS traversal algorithm to go through the entier network and look for the valves that has to be closed.
