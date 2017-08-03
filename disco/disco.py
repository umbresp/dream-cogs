import discord
import time
from discord.ext import commands
from random import choice, randint
import cogs.utils
import asyncio
from cogs.utils import checks

class disco:
    """Changes a role's color every x seconds. Must be 60 or superior."""

    def __init__(self, bot):
        self.bot = bot
	
	
	

    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def disco(self, ctx, interval:float, *, role):
        """Changes a role's color every x seconds. Must be 60 or superior."""
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)
        if not roleObj:
            no = discord.Embed(title="{} is not a valid role".format(role))
            await self.bot.say(embed=no)
            return
        if interval < 60:
            interval = 60
        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)

    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def stopdisco(self, ctx, *, role):
        """Stops the disco. A bit hacky"""
        while True:
            await self.bot.edit_role(ctx.message.server, roleObj, colour=discord.Colour(value=000000))
            await asyncio.sleep(1)
	
	
def setup(bot):
    n = disco(bot)
    bot.add_cog(n)
