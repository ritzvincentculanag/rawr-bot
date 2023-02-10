from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed


class Lyrics(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def lyrics(self, ctx, song, artist):
        pass
