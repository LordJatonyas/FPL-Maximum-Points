from fpl import FPL # type: ignore
import aiohttp
import requests
from typing import List, Optional

class PlayerStats():
    def __init__(self, user_id: Optional[str], email: Optional[str], password: Optional[str]):
        self.user_id = user_id
        self.email = email
        self.password = password
    
    async def get_players(self) -> List[tuple]:
        # Basic access to FPL API
        session = aiohttp.ClientSession()
        fpl = FPL(session)
        await fpl.login(self.email, self.password)
        user = await fpl.get_user(self.user_id)
        team = await user.get_team()

        # variables
        base_url: str = "https://fantasy.premierleague.com/api/"
        players: List[tuple] = []
        player_position: str = ""
        is_starting: bool = True
        is_captain: bool = False
        player_score: int = 0
        p_count: int = 0
        
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

            r = requests.get(f"{base_url}element-summary/{player_id}/").json()
            player_score = r.get("history")[-1].get("total_points")
            players.append((player_name, player_position, is_starting, is_captain, player_score))

        await session.close()
        return players