from fpl import FPL
import aiohttp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TEAM_ID = os.getenv("TEAM_ID")

async def my_team(user_id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login(EMAIL, PASSWORD)
        user = await fpl.get_user(user_id)
        team = await user.get_team()
        gk = list()
        df = list()
        md = list()
        fw = list()
        for p in team:
            player_id = p.get("element")
            player = await fpl.get_player(player_id, include_summary=True)
            player_firstname = getattr(player, "first_name")
            player_secondname = getattr(player, "second_name")
            player_name = f'{player_firstname} {player_secondname}'
            player_position = getattr(player, "element_type")
            if player_position == 1:
                gk.append(player_name)
            elif player_position == 2:
                df.append(player_name)
            elif player_position == 3:
                md.append(player_name)
            else:
                fw.append(player_name)
    print(gk)
    print(df)
    print(md)
    print(fw)

async def main():
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    player = await fpl.get_player(301)
    print(player)
    await session.close()

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(my_team(TEAM_ID))