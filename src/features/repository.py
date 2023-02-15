import os
import discord

from discord.ext.commands import command
from discord.ext.commands import Cog
from discord import (
    Embed,
    Colour
)


class Repository(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def ghrepo(self, ctx):
        pass
