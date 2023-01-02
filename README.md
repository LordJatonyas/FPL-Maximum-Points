# Maximum Points
This is an idea for a new "Power-Up" in Fantasy Premier League (FPL).
This "Power-Up" will be called "Maximum Points" and it takes your team for the current game week and rearranges it to generate the maximum points possible

Specifically, it will:
1) Captain the top-scoring player in your team
2) Substitute higher-scoring players into your team

The second part can only happen if it abides by the basic rules of FPL:
- Minimum number of defenders = 3
- Minimum number of midfielders = 2
- Minimum number of strikers = 1


The algorithm for deciding maximum possible points for the given game week will require actual data from your week's picks. This means using the fpl API to collect the information of a given user and then preparing the data such that it will be in a suitable format to use in the algorithm.
