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
        if not self.username_is_valid(ctx, username):
            return

        gh_user = self.gh.get_user(username[0])
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
        if not self.username_is_valid(ctx, username):
            return

        gh_user = self.gh.get_user(username[0])

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

    async def username_is_valid(self, ctx, *username) -> bool:
        if len(username) <= 0:
            await ctx.send(
                content="Please follow the format `.ghuser <github-username>`",
                delete_after=10,
                ephemeral=True
            )

            return False

        try:
            self.gh.get_user(username[0])
        except Exception as exc:
            print(exc)

            await ctx.send(
                content="No user with that username found. 🦖",
                delete_after=10,
                ephemeral=True
            )

            return False
