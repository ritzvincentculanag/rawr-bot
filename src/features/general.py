from discord.app_commands.commands import command
from discord.ext.commands import Cog
from discord import (
    Interaction,
    Colour,
    Embed,
)


class Rawr(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="commands", description="Shows all commands")
    async def commands(self, interaction: Interaction):
        embed_help = Embed(
            title="Commands",
            description="Here are the commands available to use",
            colour=Colour.yellow()
        )

        await interaction.response.send_message(embed=embed_help)
