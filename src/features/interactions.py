import os
import requests
import random

from discord.ext.commands import command
from discord.ext.commands import Cog
from discord import (
    Member,
    Colour,
    Embed,
)

from src.utils.constants import *


class Interactions(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def gmorning(self, ctx, member: Member = None):
        if not await _member_is_present(ctx, member):
            return

        await ctx.send(
            content=f"Hey {member.mention}! " \
                    f"{ctx.message.author.mention}" \
                    f" said good morning ☀",
        )

    @command()
    async def gnight(self, ctx, member: Member):
        if not await _member_is_present(ctx, member):
            return

        await ctx.send(
            content=f"Hey {member.mention}! " \
                    f"{ctx.message.author.mention}" \
                    f" said good night 🌙",
        )

    @command()
    async def slap(self, ctx, member: Member):
        if not await _member_is_present(ctx, member):
            return

        slapper = ctx.message.author.display_name
        slapped = member.display_name

        embed_slap = Embed(
            title=f"{slapper} slapped {slapped} 😲",
            description="Oh no, someone slapped you!",
            colour=Colour.green()
        )
        embed_slap.set_footer(text=CREATED_BY)
        embed_slap.set_image(url=_get_gif("slap"))

        await ctx.send(embed=embed_slap)


async def _member_is_present(ctx, member: Member) -> bool:
    if member is None:
        await ctx.send(
            content="No member selected!",
            delete_after=5,
            ephemeral=True
        )

        return False

    return True


def _get_gif(query):
    req_url = f"{BASE}" \
              f"{API}{os.environ.get('GIPHY_TOKEN')}" \
              f"{Q}{query}" \
              f"{LIMIT}" \
              f"{OFFSET}" \
              f"{RATING}" \
              f"{LANG}"

    # Request data from url
    req_data = requests.get(req_url).json()

    # Get random item from objects of data
    random_data = random.choice(req_data[""
                                         "data"])
    # Return the original media link of gif
    return random_data["images"]["original"]["url"]
