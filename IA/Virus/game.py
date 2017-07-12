from VirusGame import VirusGame
from Player import Player
from Computer import Computer
ANS = True
def play():
    """
    """
    while True:
        print("what you want to do ? \
        \np c -> player computer\
        \np p -> player player\
        \nc p -> computer player\
        \nc c -> computer computer")
        try:
            player1_input, player2_input = input().split(" ")
        except ValueError:
            print("please enter valid value")
            continue
        if player1_input == "p":
            player1 = Player(input("what name for player 1 ?"), "rouge")
        else:
            player1 = Computer("Computer 1", "rouge")
        if player2_input == "p":
            player2 = Player(input("what name for player 2 ?"), "bleu")
        else:
            player2 = Computer("Computer 2", "bleu")
        break
    while True:
        try:
            grid_length = int(input("what is the lenght of the grid ?"))
            break
        except ValueError:
            continue

    game = VirusGame(grid_length, player1, player2)
    while game.play():
        pass
    game.print_score()
    while True:
        answer = input("do you want to play again? (true, false)").lower()
        if answer == "false":
            return False
        else:
            return True

while play():
    pass
