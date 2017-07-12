"""
describes the grid to play with
>>> g = Grid(3) # create a 3*3 grid
>>> g.add_a_pawn(Player, x, y)
True
>>> g.is_finished()
False
>>> g.give_winner() #give the player with the maximum score
Player.color
>>> g.get_empty_square()
[(x1, y1), (x2, y2)...(xn, yn)] # liste of playable square
"""

from Pawn import Pawn
class Player:
    def __init__(self, color):
        self.color = color

class Grid(object):
    """
    define the Grid of the game
    :Param: grid_lenght
    """
    def __init__(self, grid_length: int):
        self.grid_length = grid_length
        self.grid = [[Pawn(None) for dummy_i in range(grid_length)]\
                     for dummy_j in range(grid_length)]
        self.last_move = []
    def add_a_pawn(self, player, pos_x, pos_y)-> bool:
        """
        add a pawn in the grid if possible
        :Param: player: Player
                pos_x: int
                pos_y: int

        :return Value: bool
        """
        if not pos_x in range(0, len(self.grid)) \
        or not pos_y in range(0, len(self.grid)):
            return False
        if self.grid[pos_x][pos_y].color is None:
            for index_x in range(-1, 2):
                for index_y in range(-1, 2):
                    other_pos_x = pos_x + index_x
                    other_pos_y = pos_y + index_y
                    if other_pos_x < 0 or other_pos_y < 0:
                        continue
                    if other_pos_x >= self.grid_length or other_pos_y >= self.grid_length:
                        continue
                    if not self.grid[other_pos_x][other_pos_y].color is None:
                        self.grid[other_pos_x][other_pos_y].change_color(player.color)
            self.grid[pos_x][pos_y].change_color(player.color)
            self.last_move.append((pos_x, pos_y))
            return True
        else:
            return False

    def is_finished(self)-> bool:
        """
        test if grid is finished
        :Param:

        :return Value: bool
        """
        for line in self.grid:
            for pawn in line:
                if pawn.color is None:
                    return False
        return True

    def give_winner(self)-> "Player":
        """
        give the winner
        :Param:

        :return Value: Player
        """
        player_score = {}
        for line in self.grid:
            for pawn in line:
                player_score[pawn.color] = player_score.get(pawn.color, 0) + 1
        return max(player_score)

    def cancel_move(self):
        if self.last_move == []:
            return False
        #print(self.last_move)
        move_to_cancel = self.last_move.pop()
        for index_x in range(-1, 2):
            for index_y in range(-1, 2):
                other_pos_x = move_to_cancel[0] + index_x
                other_pos_y = move_to_cancel[1] + index_y
                if other_pos_x < 0 or other_pos_y < 0:
                    continue
                if other_pos_x >= self.grid_length or other_pos_y >= self.grid_length:
                    continue
                #print(other_pos_x, other_pos_y)
                self.grid[other_pos_x][other_pos_y].cancel()
    def __repr__(self):
        msg = ""
        for index_x in range(len(self.grid)):
            for index_y in range(len(self.grid[index_x])):
                msg += str(self.grid[index_x][index_y]) + " "
            msg += "\n"
        return msg

    def get_empty_square(self) -> list:
        """
        give a list of tuple that contain the playable coordinate
        :Param:

        :return Value: list of tuple
        """
        empty_square = []
        for line_index in range(len(self.grid)):
            for col_index in range(len(self.grid[line_index])):
                if self.grid[line_index][col_index].color is None:
                    empty_square.append((line_index, col_index))

        return empty_square


if __name__ == "__main__":
    g = Grid(4)
    p1 = Player("rouge")
    p2 = Player("blue")
    p1.adversary = p2
    p2.adversary = p1
    #print(g)
    g.add_a_pawn(p2, 0, 3)
    g.cancel_move()
    print(g)
    """
    c = p1
    for index_x in range(0, 4):
        for index_y in range(0, 4):
            g.add_a_pawn(p1, index_x, index_y)
            g.cancel_move()
            print(g)
            c = c.adversary
    print(g)
    """
    #"""