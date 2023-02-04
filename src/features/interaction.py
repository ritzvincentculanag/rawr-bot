from discord.app_commands.commands import command
from discord.ext.commands import Cog
from discord import (
    Interaction,
    Member,
    Colour,
    Embed,
)


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
