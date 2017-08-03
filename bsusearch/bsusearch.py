from discord.ext import commands
import discord
from cogs.utils import checks
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions



class Bsusearch(object):
    """Might be merged with the CR cog soon."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bsusearch")
    async def bsusearch(self, *, search_terms):
        """Search for a deck on BSU! Special thanks to @Dark Knight#0036 for the inspiration."""

        await self.bot.say("You searched for: " + search_terms)
        search_terms = search_terms.replace(" ", "+")
        await self.bot.say("https://www.brawlstarsup.com/?s=" + search_terms)


def setup(bot):
    n = Bsusearch(bot)
    bot.add_cog(n)
