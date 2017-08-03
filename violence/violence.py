import discord
from discord.ext import commands

class Violence:
    """Useless custom cog that you can use to express your anger!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hit(self, user : discord.Member):
        """Hit someone."""

        
        await self.bot.say("-hits " + user.mention + " repeatedly-")

    @commands.command()
    async def shoot(self, user : discord.Member):
        """Shoot someone."""

        
        await self.bot.say("-shoots " + user.mention + " repeatedly-")


    @commands.command()
    async def exterminate(self, user : discord.Member):
        """Exterminate someone."""

        
        await self.bot.say("-exterminates " + user.mention + " repeatedly-")

    @commands.command()
    async def punch(self, user : discord.Member):
        """Punch someone."""

        
        await self.bot.say("-punches " + user.mention + " repeatedly-")

    @commands.command()
    async def exterminate(self, user : discord.Member):
        """Exterminate someone."""

        
        await self.bot.say("-exterminates " + user.mention + " repeatedly-")

    @commands.command()
    async def headbutt(self, user : discord.Member):
        """Headbutt someone."""

        
        await self.bot.say("-headbutts " + user.mention + " repeatedly-")

    @commands.command()
    async def destroy(self, user : discord.Member):
        """Destroy someone."""

        
        await self.bot.say("-destroys " + user.mention + " repeatedly-")

    @commands.command()
    async def revive(self, user : discord.Member):
        """Revives someone so you can kill them again."""

        
        await self.bot.say(user.mention + " has risen from the dead!")

def setup(bot):
    bot.add_cog(Violence(bot))
