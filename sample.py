from fpl import FPL # type: ignore
import aiohttp
import asyncio
import requests, json
import os
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()
EMAIL: Optional[str] = os.getenv("EMAIL")
PASSWORD: Optional[str] = os.getenv("PASSWORD")
TEAM_ID: Optional[str] = os.getenv("TEAM_ID")

base_url: str = "https://fantasy.premierleague.com/api/"

class PlayerStats():
    def __init__(self, user_id: Optional[str], email: Optional[str], password: Optional[str]):
        self.user_id = user_id
        self.email = email
        self.password = password
    
    async def get_players(self) -> list[int]:
        players: List[int] = []
        is_starting: bool = True
        is_captain: bool = False
        p_count: int = 0
        async with aiohttp.ClientSession() as session:
            fpl = FPL(session)
            await fpl.login(self.email, self.password)
            user = await fpl.get_user(self.user_id)
            team = await user.get_team()
            for p in team:
                player_id = p.get("element")
                is_captain = p.get("is_captain")
                p_count += 1
                if p_count > 11:
                    is_starting = False
                player = await fpl.get_player(player_id, include_summary=True)
                player_name: str = f'{getattr(player, "first_name")} {getattr(player, "second_name")}'
                match getattr(player, "element_type"):
                    case 1:
                        player_position = "GK"
                    case 2:
                        player_position = "DF"
                    case 3:
                        player_position = "MD"
                    case 4:
                        player_position = "FW"
                    case _:
                        player_position = ""
                r = requests.get(f"{base_url}element-summary/{player_id}/").json()
                player_score: int = r.get("history")[-1].get("total_points")
                players.append(player_score)
                """
                players.append({
                    "name": player_name,
                    "position": player_position,
                    "is_starting": is_starting,
                    "is_captain": is_captain,
                    "score": player_score
                    })
                """
            gw = r.get("history")[-1].get("round")
        return players


"""
async def main():
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    player = await fpl.get_player(301)
    print(player)
    await session.close()
"""

if __name__ == "__main__":
    ps = PlayerStats(TEAM_ID, EMAIL, PASSWORD)
    plist = asyncio.run(ps.get_players())
    print(plist)