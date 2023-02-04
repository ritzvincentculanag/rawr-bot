import os

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import (
    Embed,
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

        for index, server in enumerate(self.servers):
            embed_servers.add_field(
                name=f"{server.domain}",
                value=f"""
                Address: `{server.address}`
                Status: `{server.status}`
                Players: `{server.players_count}`
                Index: `{index}`
                """.strip()
            )

        await ctx.send(embed=embed_servers)

    @command()
    async def mcstart(self, ctx, index: int):
        if not await self._server_index_valid(ctx, index):
            return

        server_to_start = self.servers[index]
        if server_to_start.status == "online":
            await ctx.send(
                content="Server is already online",
                delete_after=5,
                ephemeral=True
            )
            return

        embed_start = Embed(
            title=f"Starting {server_to_start.domain}",
            colour=Colour.orange()
        )
        embed_start.set_author(name="Aternos")
        embed_start.set_footer(text=CREATED_BY)

        await ctx.send(embed=embed_start)

        server_to_start.start()

    @command()
    async def mcstop(self, ctx, index: int):
        if not await self._server_index_valid(ctx, index):
            return

        server_to_stop = self.servers[index]
        if server_to_stop.status == "offline":
            await ctx.send(
                content="Server is already offline",
                delete_after=5,
                ephemeral=True
            )
            return

        embed_stop = Embed(
            title=f"Stopping {server_to_stop.domain}",
            colour=Colour.orange()
        )
        embed_stop.set_author(name="Aternos")
        embed_stop.set_footer(text=CREATED_BY)

        await ctx.send(embed=embed_stop)

        server_to_stop.stop()

    @command()
    async def mcstatus(self, ctx, index: int):
        if not await self._server_index_valid(ctx, index):
            return

        server_show = self.servers[index]
        server_show.fetch()
        embed_status = Embed(
            title=f"Status of {server_show.domain}",
            description=f"""
            Status: `{server_show.status}`
            Players: `{server_show.players_count}`
            Version: `{server_show.version}`
            Edition: `{'Java' if server_show.is_java else 'Bedrock'}`
            """.strip(),
            colour=Colour.green()
        )
        embed_status.set_author(name="Aternos")
        embed_status.set_footer(text=CREATED_BY)

        await ctx.send(embed=embed_status)

    @command()
    async def mcplayers(self, ctx, index: int):
        if not await self._server_index_valid(ctx, index):
            return

        if len(self.servers[index].players_list) <= 0:
            await ctx.send(
                content="There are no players at the moment.",
                delete_after=5,
                ephemeral=True
            )

            return

        server_selected = self.servers[index]
        server_players = server_selected.players_list
        embed_players = Embed(
            title=f"{server_selected.domain} players",
            colour=Colour.blue()
        )

        all_players = ""
        for player in server_players:
            all_players += f"`{player}`\n"

        embed_players.set_author(name="Aternos")
        embed_players.set_footer(text=CREATED_BY)
        embed_players.add_field(
            name=f"Player count: {server_selected.players_count}",
            value=all_players
        )

        await ctx.send(embed=embed_players)

    async def _server_index_valid(self, ctx, index: int):
        if index >= len(self.servers):
            await ctx.send(
                content="Invalid server index",
                delete_after=5,
                ephemeral=True
            )

            return False

        return True
