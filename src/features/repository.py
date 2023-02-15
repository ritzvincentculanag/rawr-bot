import os

from discord.ext.commands import command, CommandInvokeError
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

        try:
            gh_user = self.gh.get_user(username[0])
        except Exception as exc:
            print(exc)

            await ctx.send(
                content="No user with that username found. 🦖",
                delete_after=10,
                ephemeral=True
            )

            return

        embed_user = Embed(
            title=f"{gh_user.login if gh_user.name == '' else gh_user.name}",
            description=f"""
            *{gh_user.login}*
            {gh_user.bio}
            
            Followers: `{gh_user.followers}`
            Public Repos: `{gh_user.public_repos}`
            """.strip(),
            colour=Colour.blue(),
            url=gh_user.url
        )
        embed_user.set_thumbnail(url=gh_user.avatar_url)
        embed_user.set_author(name="GitHub", url=gh_user.url, icon_url=gh_user.avatar_url)
        embed_user.set_footer(text=CREATED_BY)

        for repo in gh_user.get_repos():
            embed_user.add_field(name=repo.name, value=repo.description, inline=False)

        await ctx.send(embed=embed_user)

    @command()
    async def ghrepos(self, ctx, *username):
        if len(username) <= 0:
            await ctx.send(
                content="Please follow the format `.ghuser <github-username>`",
                delete_after=10,
                ephemeral=True
            )

            return

        try:
            gh_user = self.gh.get_user(username[0])
        except Exception as exc:
            print(exc)

            await ctx.send(
                content="No user with that username found. 🦖",
                delete_after=10,
                ephemeral=True
            )

            return

        repositories = gh_user.get_repos()

        embed_repos = Embed(
            title=f"{gh_user.name if gh_user.name else gh_user.login}'s Repositories",
            colour=Colour.blue(),
            url=gh_user.repos_url
        )
        embed_repos.set_author(name="GitHub")
        embed_repos.set_footer(text=CREATED_BY)

        for repo in repositories:
            embed_repos.add_field(
                name=f"{repo.name}",
                value=f"""
                {repo.description if repo.description else 'No description...'}
                [Visit repository]({repo.url})
                """.strip(),
                inline=False,
            )

            print(repo.name)

        await ctx.send(embed=embed_repos)

