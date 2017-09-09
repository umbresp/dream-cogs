from discord.ext import commands

class Regional(object):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="regional")
    async def _regional(self, *, text):
        text = text.lower()
        x = 0
        while x <= len(text):
            msg += ":regional_indicator_" + text[x]
        
        if len(msg) > 2000:
            await self.bot.say("Your message is too long.")
        else:
            await self.bot.say(msg)


def setup(bot):
    n = Regional(bot)
    bot.add_cog(n)
