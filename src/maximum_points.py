class MaximumPoints():
    def __init__(self, gk, df, md, fw):
        self.gk = gk
        self.df = sorted(df)
        self.md = sorted(md)
        self.fw = sorted(fw)

    def maxGK(self):
        return max(self.gk[0], self.gk[-1])

    def maxOutfield(self):
        bestPoints = 0
        # necessary conditions (3 defenders, 2 midfielders, 1 forward)
        bestPoints += self.df[-1] + self.df[-2] + self.df[-3]
        bestPoints += self.md[-1] + self.md[-2]
        bestPoints += self.fw[-1]

        remaining = []
        for i in range(len(self.df) - 3):
            remaining.append(self.df[i])
        for j in range(len(self.md) - 2):
            remaining.append(self.md[j])
        for k in range(len(self.fw) - 1):
            remaining.append(self.fw[k])
        remaining.sort()

        for x in range(len(remaining) - 4, len(remaining)):
            bestPoints += remaining[x]
        return bestPoints

    def maxPoints(self):
        return self.maxGK() + self.maxOutfield()

def main():
    gk = [7,2]
    df = [2,2,14,5,6]
    md = [3,3,3,7,10]
    fw = [9,13,5]
    maximise = MaximumPoints(gk, df, md, fw)
    print(maximise.maxGK())
    print(maximise.maxOutfield())
    print(maximise.maxPoints())
    return 0

if __name__ == "__main__":
    main()
