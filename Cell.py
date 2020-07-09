Created on Fri Mar  6 16:40:29 2020
@author: Matt Burns
Description: Cell Class for Maze Building and Flooding Algorithm
"""

import math

class Cell:
    def __init__(self, x, y):
        a = round(math.sqrt((7-x) * (7-x) + (7-y) * (7-y)), 2)
        b = round(math.sqrt((7-x) * (7-x) + (8-y) * (8-y)), 2)
        c = round(math.sqrt((8-x) * (8-x) + (7-y) * (7-y)), 2)
        d = round(math.sqrt((8-x) * (8-x) + (8-y) * (8-y)), 2)
        self.distance = min(a, b, c, d)
        self.checked = False
        self.north_wall = False
        self.south_wall = False
        self.west_wall = False
        self.east_wall = False
        self.available = True
        self.step = 0

    def set_checked(self, status):
        """ Set this cell whether having been previously traversed or not """
        self.checked = status

    def set_north_wall(self, status):
        """ Set the status of north wall of this cell as existing or not """
        self.north_wall = status

    def set_south_wall(self, status):
        """ Set the status of south wall of this cell as existing or not """
        self.south_wall = status

    def set_west_wall(self, status):
        """ Set the status of west wall of this cell as existing or not """
        self.west_wall = status

    def set_east_wall(self, status):
        """ Set the status of east wall of this cell as existing or not """
        self.east_wall = status

    def set_unavailable(self):
        """ Set this cell as being unavailable for traversing """
        self.available = False

    def set_step(self, val):
        """ Set the steps needed to get from the origin to this cell """
        self.step = val

