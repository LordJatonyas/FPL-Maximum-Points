from fpl import FPL # type: ignore
import aiohttp
from operator import itemgetter
import requests
from typing import Optional
import maximum_points

import asyncio

class PlayerStats():
    def __init__(self, user_id: Optional[str], email: Optional[str], password: Optional[str]):
        self.user_id = user_id
        self.email = email
        self.password = password
    
    # Output is a list with index 0 -> GK, 1 -> DF, 2 -> MD, 3 -> FW
    # Each index has a list of tuples (name, score)
    async def get_players(self) -> list[list[tuple]]:
        # return variable
        players: list[list[tuple]] = [[],[],[],[]]

        # Basic access to FPL API, including fail cases
        session = aiohttp.ClientSession()
        fpl = FPL(session)
        try:
            await fpl.login(self.email, self.password)
        except:
            print("Invalid email or password")
            await session.close()
            return players
        
        user = await fpl.get_user(self.user_id)
        try:
            team = await user.get_team()
        except:
            print("Invalid user ID")
            await session.close()
            return players


        # variables
        base_url: str = "https://fantasy.premierleague.com/api/"
        player_id: int = 0
        player_position: int = 0
        player_name: str = ""
        player_score: int = 0
        
        for p in team:
            player_id = p.get("element")
            player = await fpl.get_player(player_id, include_summary=True)
            r = requests.get(f"{base_url}element-summary/{player_id}/").json()

            player_position = getattr(player, "element_type") - 1
            player_name = f'{getattr(player, "first_name")} {getattr(player, "second_name")}'
            try:
                player_score = r.get("history")[-1].get("total_points")
            except:
                print("Game hasn't started!")
                await session.close()
                return players

            players[player_position].append((player_name, player_score))

        await session.close()

        for i in range(len(players)):
            players[i].sort(key=itemgetter(1))

        return players

if __name__ == "__main__":
    team_id: str = input("Enter your team ID: ")
    email: str = input("Enter the email address tied to FPL: ")
    password: str = input("Enter your password: ")
    ps = PlayerStats(team_id, email, password)
    players: list[list[tuple]] = asyncio.run(ps.get_players())
    print(f'{players}\n')
    object1 = maximum_points.MaximumPoints(players)
    print(object1.maxTeam())
    print(object1.maxScore())