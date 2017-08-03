import discord
import time
from discord.ext import commands
from random import choice, randint
import cogs.utils
import asyncio
from cogs.utils import checks

class disco:
    """Changes a role's color every x seconds. Must be 60 or superior. Based off MasterKnight's cog"""

    def __init__(self, bot):
        self.bot = bot

	
    stopped = false
	
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def disco(self, ctx, seconds:float, *, role):
        """Changes a role's color every x seconds. Must be 60 or superior."""
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)
	
        if not roleObj:
            no = discord.Embed(title="{} is not a valid role".format(role))
            await self.bot.say(embed=no)
            return

        if interval < 60:
            await self.bot.say("The interval must be higher than 60.")
	    return
	
	await self.bot.say("{} is now disco!".format(role))
	
        while not stopped:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)

    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def stopdisco(self, ctx, *, role):
        """Stops the disco. Not sure if it works"""
	
        stopped = true
	
	
def setup(bot):
    n = disco(bot)
    bot.add_cog(n)
