import discord
import time
from discord.ext import commands
from random import choice, randint
import cogs.utils
import asyncio
from cogs.utils import checks
from .utils.dataIO import fileIO
from __main__ import send_cmd_help
import os

class disco:
    """Changes a role's color every x seconds. Must be 60 or superior. Based off MasterKnight's cog"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO("data/disco/settings.json", "load")

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
            

    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def stopdisco(self, ctx, *, role):
        """DOESN'T DO ANYTHING!! DOESN'T WORK!! DON'T USE!!"""

        stopped = 1
        await self.bot.say("{} is no longer disco!".format(role))
        
        
    async def change_role_color(self, message):
        for roles in settings:
            await self.bot.edit_role(message.server, roles, color=discord.Colour(value=random_color(message)))
            
        await asyncio.sleep(60)
        
    def random_color(self, msg):
        color = "".join([choice('0123456789ABCDEF') for x in range(6)])
        return color
   
        
        
def check_folders():
    if not os.path.exists("data/disco"):
        print("Creating data/disco folder...")
        os.makedirs("data/disco")

def check_files():
    settings = {}

    f = "data/disco/settings.json"
    if not fileIO(f, "check"):
        print("Creating empty settings.json...")
        fileIO(f, "save", settings)

def setup(bot):
    check_folders()
    check_files()
    n = disco(bot)
    bot.add_listener(n.change_role_color, "on_message")
    bot.add_cog(n)
