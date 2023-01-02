# Input will be 2 arrays: 1. Current Team, 2. Bench
# Output will be an array of Changes made

class WeekMaximiser:
    def __init__(self, team=None, bench=None):
        self.team = team
        self.bench = bench

    # Sort Players based on Points (non-decreasing)
    # If any outfield player on the bench has higher score than first player in sorted array:
    # Check if it's a valid replacement, if valid, replace
    # If invalid, move to next sub
    def 
