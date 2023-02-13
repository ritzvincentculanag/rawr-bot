import os

from discord.ext.commands import Bot
from discord import Intents

from dotenv import load_dotenv

# Import cogs
from features.general import Rawr
from features.interactions import Interactions
from features.chatgpt import Chatgpt
from features.aternos import Aternos
from features.song import Lyrics

# Bot intents
bot_intents = Intents.default()
bot_intents.message_content = True

# Create Bot instance
bot = Bot(command_prefix=".", intents=bot_intents)

# Declare cots
bot_cogs = [
    Rawr,
    Interactions,
    Chatgpt,
    Lyrics
]


@bot.event
async def on_ready():
    # Add all cogs to bot
    for cog in bot_cogs:
        await bot.add_cog(cog(bot))

    # Refresh all commands in tree
    await bot.wait_until_ready()
    await bot.tree.sync()

    print("🤖 Bot is now online")


if __name__ == '__main__':
    load_dotenv()

    bot.run(os.environ.get("DISCORD_TOKEN"))
