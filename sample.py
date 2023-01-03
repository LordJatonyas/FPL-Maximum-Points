from fpl import FPL
import aiohttp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

async def my_team(user_id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login(EMAIL, PASSWORD)
        user = await fpl.get_user(user_id)
        team = await user.get_team()
        player_id = team[0]["element"]
        player = await fpl.get_player(player_id, include_summary=True)
        total_points = getattr(player, "total_points", 0.0)
    print(total_points)

async def main():
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    player = await fpl.get_player(301)
    print(player)
    await session.close()

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(my_team(4905776))