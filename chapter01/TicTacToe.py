#######################################################################
# Copyright (C)                                                       #
# 2016 Shangtong Zhang(zhangshangtong.cpp@gmail.com)                  #
# 2016 Jan Hakenberg(jan.hakenberg@gmail.com)                         #
# 2016 Tian Jun(tianjun.cpp@gmail.com)                                #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

from __future__ import print_function

from chapter01.Judger import Judger
from chapter01.State import getAllStates
from chapter01.players import HumanPlayer, Player

# all possible board configurations
allStates = getAllStates()


def train(epochs=20000):
    player1 = Player(allStates)
    player2 = Player(allStates)
    judger = Judger(allStates, player1, player2, feedback=True)
    player1Win = 0.0
    player2Win = 0.0
    for i in range(0, epochs):
        if i > 0 and i % 1000 == 0:
            print("Epoch", i, player1Win / i, ":", player2Win / i)
        winner = judger.play()
        if winner == 1:
            player1Win += 1
        if winner == -1:
            player2Win += 1
        judger.reset()
    print(player1Win / epochs)
    print(player2Win / epochs)
    player1.savePolicy()
    player2.savePolicy()


def compete(turns=500):
    player1 = Player(allStates, exploreRate=0)
    player2 = Player(allStates, exploreRate=0)
    judger = Judger(allStates, player1, player2, feedback=False)
    player1.loadPolicy()
    player2.loadPolicy()
    player1Win = 0.0
    player2Win = 0.0
    for i in range(0, turns):
        if i % 100 == 0:
            print("Epoch", i)
        winner = judger.play()
        if winner == 1:
            player1Win += 1
        if winner == -1:
            player2Win += 1
        judger.reset()
    print(player1Win / turns)
    print(player2Win / turns)


def play():
    while True:
        player1 = Player(allStates, exploreRate=0)
        player2 = HumanPlayer()
        judger = Judger(allStates, player1, player2, feedback=False)
        player1.loadPolicy()
        judger.currentState.show()
        winner = judger.play(show=True)
        if winner == player2.symbol:
            print("Win!")
        elif winner == player1.symbol:
            print("Lose!")
        else:
            print("Tie!")


if __name__ == "__main__":
    train(epochs=20000)
    compete(turns=500)
    play()
