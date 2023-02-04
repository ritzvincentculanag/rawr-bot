import os

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import (
    Embed,
    Member,
    Colour
)

from python_aternos import Client

from src.utils.constants import *


class Aternos(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = Client.from_credentials(
            username=os.environ.get("ATERNOS_USERNAME"),
            password=os.environ.get("ATERNOS_PASSWORD")
        )
        self.servers = self.client.list_servers()

    @command()
    async def mcservers(self, ctx):
        embed_servers = Embed(title="Servers", colour=Colour.green())
        embed_servers.set_author(name="Aternos")
        embed_servers.set_footer(text=CREATED_BY)

        for server in self.servers:
            embed_servers.add_field(
                name=f"{server.domain}",
                value=f"""
                Address: `{server.address}`
                Status: `{server.status}`
                Players: `{server.players_count}`
                """.strip()
            )

        await ctx.send(embed=embed_servers)
