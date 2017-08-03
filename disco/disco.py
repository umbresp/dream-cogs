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

    global stopped
    stopped = 0

    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def disco(self, ctx, seconds:float, *, role):
        """Changes a role's color every x seconds. Must be 60 or superior."""
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)

        stopped = 0

        if not roleObj:
            no = discord.Embed(title="{} is not a valid role".format(role))
            await self.bot.say(embed=no)
            return
 
        if seconds < 60:
            await self.bot.say("The interval must be higher than 60.")
            return

        await self.bot.say("{} is now disco!".format(role))

        while stopped == 0:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(seconds)

    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def stopdisco(self, ctx, *, role):
        """DOESN'T DO ANYTHING!! DOESN'T WORK!! DON'T USE!!"""

        stopped = 1
        await self.bot.say("{} is no longer disco!".format(role))

def setup(bot):
    n = disco(bot)
    bot.add_cog(n)
