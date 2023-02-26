import os
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
        openai.api_key = os.environ.get("OPENAI_TOKEN")

    @command()
    async def chat(self, ctx):
        if not await command_is_valid(
                ctx=ctx,
                prefix=".chat",
                content=ctx.message.content):
            return

        question_initial = ctx.message.content.lower() \
            .replace(".chat ", "")
        question_openai = question_initial.replace(" ", "-")
        question_title = question_initial.title()
        question_data = openai.Completion.create(
            prompt=question_openai,
            model=DAVINCI,
            temperature=0.8,
            max_tokens=1000
        )
        question_answer = question_data["choices"][0]["text"]

        embed_answer = Embed(
            title=question_title,
            description=question_answer,
            colour=Colour.green()
        )
        embed_answer.set_footer(text=ANSWER_AUTHOR)

        await ctx.reply(embed=embed_answer)

    @command()
    async def generate(self, ctx):
        if not await command_is_valid(
                ctx=ctx,
                prefix=".generate",
                content=ctx.message.content):
            return

        generate_initial = ctx.message.content.lower() \
            .replace(".generate ", "")
        generate_image_caption = generate_initial.title()

        try:
            generated_image = openai.Image.create(
                prompt=generate_image_caption,
                size="512x512",
                n=1
            )
        except Exception as e:
            print(e)
            await ctx.reply(
                content="Error: Your text may contain harmful words. Try again.",
                delete_after=10,
                ephemeral=True
            )

            return

        generate_image_url = generated_image["data"][0]["url"]

        embed_image = Embed(
            title=generate_image_caption,
            description="Here's the image!",
            colour=Colour.green()
        )

        embed_image.set_footer(text=ANSWER_AUTHOR)
        embed_image.set_image(url=generate_image_url)

        await ctx.reply(embed=embed_image)


async def command_is_valid(ctx, prefix, content) -> bool:
    command_to_check = content.replace(prefix, "")

    if not command_to_check:
        await ctx.send(
            content="Please enter a valid argument...",
            delete_after=10,
            ephemeral=True
        )

        return False

    return True
