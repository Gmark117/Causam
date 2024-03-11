'''
Movements:
- Pieces move between points along the lines
- White pieces causes one piece adjacent to their new position to move one step to the left (One level lower)
- Black pieces causes one piece adjacent to their new position to move one step to the right (One level higher)
- The Black high piece causes one piece adjacent to their new position to move one step to the right OR to the left (Player Choice)

Rules:
- All semi-circles at the end are filled by White pieces     --> WHITE WINS
- All non semi-circles at the end are filled by White pieces --> BLACK WINS
- Pieces cannot move from the last level
- Black pieces cannot occupy the last level
- Multiple pieces cannot occupy the same node
- You cannot displace a piece as an effect of your move if the destination node is occupied
'''

import Assets

def get_next_nodes(selection, next_nodes):
    # Return next viable nodes
    pass