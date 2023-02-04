from discord.ext.commands import command
from discord.ext.commands import Cog
from discord import Colour, Embed


class Rawr(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def commands(self, ctx):
        embed_help = Embed(
            title="Commands",
            description="Here are the commands available to use",
            colour=Colour.yellow()
        )

        await ctx.send(embed=embed_help)
