# MazeSolver
Python maze solver with GUI using different search algorithms.
Identifies the best path to navigate terrain when using UCS and A*. 

Requirements:  
1. pygame install 

To install pygame: 
```bash
pip install pygame
```

2. All source files used are included in this repository 

HOW TO USE THE PROGRAM: 

User can click on any combination of SEARCH ALGORITHM (DFS, UCS, A*) and
MAZE NUMBER (1, 2, 3), then click RUN. 

Once a search algorithm has executed, use the ARROW KEYS to traverse the 
maze. Straying from the optimal path will cause the search algorithm to 
rerun and construct a new optimal path.

Note: Since DFS does not display an optimal path, using the ARROW KEYS
will always cause the algorithm to rerun

Note: Multiple presses of the ARROW KEYS will queue those transitions,
causing the search algorithm to run again for each node visited while not 
on the optimal path. 

Press RESET to reset the maze, clearing any paths drawn, and returning 
to the original start node position. 