"""
"""
import random
#import time

from Player import Player
from Grid import Grid
#from Pawn import Pawn #useless since i don't use copygrid
from Tree import Tree


class Computer(Player):
    """
    """
    def __init__(self, player_name, player_color, depth=3):
        """
        """
        Player.__init__(self, player_name, player_color)
        self.turn = 0
        self.depth = depth -1
        self.player_pawn = 1
        self.opponent_pawn = 1
        self.player_win = 50
        self.opponent_win = -50
        self.player_locked = 5
        self.opponent_locked = 5
        self.depth_player = 1
        self.depth_opponent = -1
        self.tree = Tree()

    def play(self, grid: Grid):
        """
        """
        #print(self.name)
        empty_square = grid.get_empty_square()
        max_value = -float('inf')
        best_move = []

        for available_pos_index, available_pos in enumerate(empty_square):
            #print(possible_grid[possible_result_index])
            grid.add_a_pawn(self, available_pos[0], available_pos[1])
            value, branch = self.minmax(grid, self.depth, self.adversary)
            branch.set_pos(available_pos)
            self.tree.add(branch)
            if value > max_value:
                max_value = value
                best_move = [empty_square[available_pos_index]]
            elif value == max_value:
                best_move.append(empty_square[available_pos_index])
            grid.cancel_move()

        self.tree.set_value(max_value)
        pos = random.choice(best_move)
        #print(self.color, best_move, len(best_move), len(empty_square))
        self.turn += 1
        self.tree.write_in_file("./tree/tree " + str(self.name)+ str(self.turn) + " turn")
        self.tree = Tree()
        return pos



    def minmax(self, grid: Grid, depth: int, player: Player)-> int:
        """
        """
        current_tree = Tree()
        if grid.is_finished() or depth == 0:

            #print(grid, "val :", self.eval(grid, depth), "player",player)
            value = self.eval(grid, depth)
            current_tree.set_value(value)
            #grid.cancel_move()
            return value, current_tree

        empty_square = grid.get_empty_square()

        if player.color == self.color:
            value = []
            for available_pos in empty_square:
                grid.add_a_pawn(self, available_pos[0], available_pos[1])
                current_value, branch = self.minmax(grid, depth-1, player.adversary)
                branch.set_pos(available_pos)
                current_tree.add(branch)
                value.append(current_value)
                grid.cancel_move()

            value = max(value)
            current_tree.set_value(value)
            return value, current_tree
        else:
            value = []
            for available_pos in empty_square:
                grid.add_a_pawn(self.adversary, available_pos[0], available_pos[1])
                current_value, branch = self.minmax(grid, depth-1, player.adversary)
                branch.set_pos(available_pos)
                current_tree.add(branch)
                value.append(current_value)
                grid.cancel_move()
            value = min(value)
            current_tree.set_value(value)
            return value, current_tree

    def eval(self, grid: Grid, depth: int) -> int:
        """
        """

        #count the pawn owned by every player
        number_player = 0
        number_opponent = 0
        for pos_x, line in enumerate(grid.grid):
            for pos_y, pawn in enumerate(line):
                if pawn.color is None:
                    continue
                if pawn.color == self.color:
                    number_player += self.player_pawn
                else:
                    number_opponent += self.opponent_pawn
                if grid.is_finished():
                    continue

                surround = True
                for index_x in range(-1, 2):
                    for index_y in range(-1, 2):
                        if not surround:
                            continue
                        other_pos_x = pos_x + index_x
                        other_pos_y = pos_y + index_y
                        if other_pos_x < 0 or other_pos_y < 0:
                            continue
                        if other_pos_x >= grid.grid_length or other_pos_y >= grid.grid_length:
                            continue
                        if grid.grid[other_pos_x][other_pos_y].color is None:
                            surround = False
                if surround:
                    if grid.grid[pos_x][pos_y].color == self.color:
                        number_player += self.player_locked
                    else:
                        number_opponent += self.opponent_locked

        #test if the game is finished
        if grid.is_finished():
            if number_player > number_opponent:
                return self.player_win + depth * self.depth_player + number_player * self.player_locked
            else:
                return self.opponent_win + depth * self.depth_opponent + number_opponent * self.player_locked
        return number_player - number_opponent



    