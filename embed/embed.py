from redbot.core import commands, checks, Config
from redbot.core.utils.predicates import ReactionPredicate, MessagePredicate
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu
import contextlib
import discord

class embed(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("embed=discord.Embed(title="CRZA", url="https://discordnitro.gq/", description="Big Fruad", color=0xff3333)
embed.set_author(name="CRZA", url="https://www.discordnitro.gq/",, icon_url="https://avatars3.githubusercontent.com/u/51196241?s=460&v=4")
embed.add_field(name="HELLO", value="Fruad here!", inline=True)
embed.set_footer(text="BOT BY CRZA ")
await self.bot.say(embed=embed)")
