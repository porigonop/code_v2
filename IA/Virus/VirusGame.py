"""
contain the VirusGame class:
>>>GAME = VirusGame(3, Player1, Player2)
>>>GAME.play() #for 1 turn
"""
from Grid import Grid
from Player import Player
from Computer import Computer
from computer_evolve import ComputerEvolve as CE

class VirusGame:
    """
    describe the virus game
    :Param: grille_lenght: int
            player1: Player
            Player2: Player
            no_print: bool
    """
    def __init__(self, grid_lenght: int,\
                player1: Player, player2: Player,\
                no_print=False):

        self.no_print = no_print
        self.grid = Grid(grid_lenght)
        if isinstance(player1, CE) and isinstance(player2, CE):
            self.player1 = CE("comp1", "rouge", player1.depth, player1.genes)
            self.player2 = CE("comp2", "bleu", player2.depth, player2.genes)
        else:
            self.player1 = player1
            self.player2 = player2
        self.player1.set_adversary(self.player2)
        self.player2.set_adversary(self.player1)
        self.player = self.player1

    def play(self):
        """
        launch 1 turn and add a pawn to the game
        :Param

        :Return Value: bool
        """
        if self.grid.is_finished():
            if not self.no_print:
                print(self.grid)
            return False

        if not self.no_print:
            print(self.player.name, "play on this grid")
            print(self.grid)


        pos = self.player.play(self.grid)
        self.grid.add_a_pawn(self.player, pos[0], pos[1])
        self.player = self.player.get_adversary()
        return True

    def print_score(self):
        """
        print the result of the game
        :Param

        :Return Value: str
        """
        score1, score2 = self.get_score()
        print("score", self.player1.name, score1)
        print("score", self.player2.name, score2)
        if score1 == score2:
            return "there is no winner"
        else:
            return "winner is..." + str(self.player1.name if score1 > score2 else self.player2.name)

    def get_score(self):
        """
        return the 2 score of the game
        :Param

        :Return Value: int, int
        """
        score1 = 0
        score2 = 0
        for line in self.grid.grid:
            for pawn in line:
                if pawn.color == self.player1.color:
                    score1 += 1
                else:
                    score2 += 1
        return score1, score2




if __name__ == "__main__":
    P1 = Computer("Antoine", "rouge")
    P2 = Computer("Marion", "bleu")
    GAME = VirusGame(3, P1, P2, no_print=True)
    for i in range(100):
        while GAME.play():
            pass
        GAME.print_score()
