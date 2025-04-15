# MazeSolver
Python maze solver with GUI using different search algorithms.
Identifies the best path to navigate terrain when using UCS and A*. 

### Requirements:  
1. pygame install 

To install pygame: 
```bash
pip install pygame
```

2. All source files used are included in this repository 

### HOW TO USE THE PROGRAM: 

User can click on any combination of SEARCH ALGORITHM (DFS, UCS, A*) and
MAZE NUMBER (1, 2, 3), then click RUN. 

Once a search algorithm has executed, use the ARROW KEYS to traverse the 
maze. Straying from the path that was found will cause the search algorithm to 
rerun and construct a new path.

UCS and A* find and display the optimal path from the current start location.
DFS finds and displays the [often suboptimal] path it found. 

*Note: Multiple presses of the ARROW KEYS will queue those transitions,
causing the search algorithm to run again for each node visited while not 
on the found path.*

Press RESET to reset the maze, clearing any paths drawn, and returning 
to the original start node position. 


### Description of Files: 

- main.py - Initializes the UI window and assigns functionality to UI components.
- buttons.py - Defines the button layout.
- dfs.py - Defines the DFS search algorithm function. 
- astar.py - Defines the A* search algorithm function.
- ucs.py - Defines the UCS search algorithm function. 
- grid.py - Defines to draw_grid function to update the display.
- maze.py - Defines the MazeNode class, contains the maze structures, 
          instantiates the mazes, and calculates heuristics.
- config.py - Define values including terrain costs, colors, and text fonts. 