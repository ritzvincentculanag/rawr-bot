import os
import requests
import openai

from discord.ext.commands import command
from discord.ext.commands import Cog
from discord import (
    Colour,
    Embed,
)

from src.utils.constants import *


class Chatgpt(Cog):
    def __init__(self, bot):
        self.bot = bot

        # Init openai
        openai.api_key = os.environ.get('OPENAI_TOKEN')

    @command()
    async def ask(self, ctx):
        question_initial = ctx.message.content.lower() \
            .replace(".ask ", "")
        question_openai = question_initial.replace(" ", "-")
        question_title = question_initial.title()
        question_data = openai.Completion.create(
            prompt=question_openai,
            model=DAVINCI,
            temperature=0.8,
            max_tokens=1000
        )
        print(question_data)
        question_answer = question_data["choices"][0]["text"]

        embed_answer = Embed(
            title=question_title,
            description=question_answer,
            colour=Colour.green()
        )
        embed_answer.set_footer(text=ANSWER_AUTHOR)

        await ctx.send(embed=embed_answer)
