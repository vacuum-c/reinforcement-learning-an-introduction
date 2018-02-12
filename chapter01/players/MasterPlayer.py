from chapter01 import BOARD_COLS


class MasterPlayer:
    def __init__(self):
        self.symbol = None
        self.currentState = None
        return

    def reset(self):
        return

    def setSymbol(self, symbol):
        self.symbol = symbol
        return

    def feedState(self, state):
        self.currentState = state
        return

    def feedReward(self, reward):
        return

    def takeAction(self):  # todo
        data = int(input("Input your position:"))
        data -= 1
        i = data // int(BOARD_COLS)
        j = data % BOARD_COLS
        if self.currentState.data[i, j] != 0:
            return self.takeAction()
        return i, j, self.symbol
