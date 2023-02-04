import os

from discord.app_commands.commands import command
from discord.ext.commands import Cog
from discord import (
    Interaction,
    Member,
    Colour,
    Embed,
)

from src.utils.constants import *


class Interaction(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="gmorning", description="Greet someone good morning!")
    async def gmorning(self, interaction: Interaction, member: Member):
        if member is None:
            await interaction.response.send_message(
                content="No member provided",
                delete_after=5,
                ephemeral=True
            )

            return

        await interaction.response.send_message(
            content=f"Hey {member.mention}! " \
                    f"{interaction.user.mention}" \
                    f" said good morning ☀",
        )

    @command(name="gnight", description="Greet someone good night!")
    async def gnight(self, interaction: Interaction, member: Member):
        if member is None:
            await interaction.response.send_message(
                content="No member provided",
                delete_after=5,
                ephemeral=True
            )

            return

        await interaction.response.send_message(
            content=f"Hey {member.mention}! " \
                    f"{interaction.user.mention}" \
                    f" said good night 🌙",
        )

    @command(name="slap", description="Slap someone virtually.")
    async def slap(self, interaction: Interaction, member: Member):
        if member is None:
            await interaction.response.send_message(
                content="No member selected!'",
                delete_after=5,
                ephemeral=True
            )

            return

        slapper = interaction.user.display_name
        slapped = member.display_name

        embed_slap = Embed(
            title=f"{slapper} slapped {slapped} 😲",
            description="Oh no, someone slapped you!",
            colour=Colour.green()
        )
        embed_slap.set_footer(text=CREATED_BY)

        await interaction.response.send_message(embed=embed_slap)
