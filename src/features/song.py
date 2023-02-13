from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed, Colour

from azlyrics.azlyrics import lyrics

from src.utils.constants import *


class Song(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def lyrics(self, ctx, *song):
        song_data = " ".join(song).split("-")
        song_artist = song_data[0].replace(" ", "")
        song_title = song_data[1].replace(" ", "")
        song_lyrics = ""

        for line in lyrics(song_artist, song_title):
            song_lyrics += line

        embed_lyrics = Embed(
            title=song_data[1].strip().title(),
            description=song_lyrics,
            colour=Colour.orange()
        )
        embed_lyrics.set_author(name=song_data[0].strip().title())
        embed_lyrics.set_footer(text=AZFOOTER)

        await ctx.send(embed=embed_lyrics)
