from discord.ext import commands
import discord
from cogs.utils import checks
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions



class Deck(object):
    """Might be merged with the CR cog soon."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="deck")
    async def deck(self, *, search_terms):
        """Search for a deck on CRA! Special thanks to @Dark Knight#0036 for the inspiration."""

        await self.bot.say("You searched for: " + search_terms)
        search_terms = search_terms.replace(" ", "+")
        await self.bot.say("https://www.clashroyalearena.com/?s=" + search_terms)


def setup(bot):
    n = Deck(bot)
    bot.add_cog(n)
