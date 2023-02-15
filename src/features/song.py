import os

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed, Colour

from src.utils.constants import *

from lyricsgenius import Genius


class Lyrics(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.genius = Genius(os.environ.get("GENIUS_TOKEN"))

    @command()
    async def lyrics(self, ctx, *song):
        if len(song) <= 1:
            await ctx.send(
                content="Follow the format `.lyrics <song-artist> - <song-title>`",
                delete_after=10,
                ephemeral=True
            )

            return

        song_data = " ".join(song).split("-")
        song_artist = song_data[0].strip().title()
        song_title = song_data[1].strip().title()
        song = self.genius.search_song(song_title, song_artist)

        embed_lyrics = Embed(
            title=song_title,
            description=song.lyrics,
            colour=Colour.orange()
        )

        embed_lyrics.set_author(name=song_data[0].strip().title())
        embed_lyrics.set_footer(text=AZFOOTER)

        print(song.lyrics)
        print(song)

        await ctx.send(embed=embed_lyrics)
