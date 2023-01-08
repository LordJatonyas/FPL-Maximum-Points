class MaximumPoints():
    def __init__(self, players: list[list[tuple]]):
        self.players = players # each list within is already sorted based on score

    def maxGK(self) -> tuple:
        return self.players[0][-1]

    def maxOutfield(self) -> list[list[tuple]]:
        bestOutfield: list[list[tuple]] = [[],[],[]]

        # necessary conditions (3 defenders, 2 midfielders, 1 forward)
        bestOutfield[2].append(self.players[3][-1])
        for x in range(3):
            if x < 2:
                bestOutfield[1].append(self.players[2][-x-1])
            bestOutfield[0].append(self.players[1][-x-1])

        # Remaining 4 players are picked depending on points
        # First, fill it with the remaining FW and MD (1 + 3 = 4)
        bestOutfield[2].append(self.players[3][0])
        for y in range(3):
            bestOutfield[1].append(self.players[2][2-y])
        
        # Now, compare DF list with what's just added
        for z in range(2):
            if bestOutfield[2][-1] < self.players[1][1-z] and len(bestOutfield[2]) > 1:
                bestOutfield[2].pop()
                bestOutfield[0].append(self.players[1][1-z])
                continue
            if bestOutfield[1][-1] < self.players[1][1-z] and len(bestOutfield[1]) > 2:
                bestOutfield[1].pop()
                bestOutfield[0].append(self.players[1][1-z])
                continue

        return bestOutfield

    def maxTeam(self) -> list[list[tuple]]:
        team = self.maxOutfield()
        team.insert(0, [self.maxGK()])
        return team

    def maxScore(self) -> int:
        bestScore: int = 0
        for l in self.maxTeam():
            for t in l:
                bestScore += t[1]
        return bestScore

    def draw_layout(self):
        return ""