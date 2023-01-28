class MaximumPoints():
    def __init__(self, players: list[list[tuple]]):
        self.players = players # each list within is already sorted based on score

    def checkPlayersArrayLengths(self) -> bool:
        if len(self.players[0]) != 2:
            print("There should be 2 Goalkeepers!")
            return False
        if len(self.players[1]) != 5:
            print("There should be 5 Defenders!")
            return False
        if len(self.players[2]) != 5:
            print("There should be 5 Midfielders!")
            return False
        if len(self.players[3]) != 3:
            print("There should be 3 Fowards!")
            return False
        return True


    def maxGK(self) -> tuple:
        if not self.checkPlayersArrayLengths():
            return ()
        return self.players[0][-1]

    def maxOutfield(self) -> list[list[tuple]]:
        bestOutfield: list[list[tuple]] = [[],[],[]]
        # Check that the input is correct
        if not self.checkPlayersArrayLengths():
            return bestOutfield

        # necessary conditions (3 defenders, 2 midfielders, 1 forward)
        for i in range(len(bestOutfield) - 1, -1, -1):
            for j in range(1, 4 - i):
                bestOutfield[i].append(self.players[i + 1][-j])

        # pick 4 more players



        return bestOutfield

    def pickCaptain(self) -> tuple(int):
        pass

    def maxTeam(self) -> list[list[tuple]]:
        team = self.maxOutfield()
        team.insert(0, [self.maxGK()])
        return team

    def maxScore(self) -> int:
        bestScore: int = 0
        if not self.checkPlayersArrayLengths():
            return bestScore
        for l in self.maxTeam():
            for t in l:
                bestScore += t[1]
        return bestScore

    def draw_layout(self):
        return ""
