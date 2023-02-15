import os
import discord

from discord.ext.commands import command
from discord.ext.commands import Cog
from discord import (
    Embed,
    Colour
)

from github import Github

from src.utils.constants import *


class Repository(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gh = Github(os.environ.get('GITHUB_TOKEN'))

    @command()
    async def ghuser(self, ctx, *username):
        if len(username) <= 0:
            await ctx.send(
                content="Please follow the format `.ghuser <github-username>`",
                delete_after=10,
                ephemeral=True
            )

            return

        gh_user = self.gh.get_user(username[0])
        embed_user = Embed(
            title=gh_user.name,
            description=gh_user.bio,
            colour=Colour.dark_blue(),
        )

        embed_user.set_thumbnail(url=gh_user.avatar_url)
        embed_user.set_author(name="GitHub")
        embed_user.set_footer(text=CREATED_BY)

        await ctx.send(embed=embed_user)
