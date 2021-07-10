import discord
from discord.ext import commands
import json
import random

from core.classes import Cog_Extension

from discord.ext.commands.core import bot_has_any_role, command


class Main(Cog_Extension):


    @commands.command()
    async def ping (self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} ms")

    @commands.command()
    async def hi (self,ctx):
        await ctx.send(f"456")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("入漏野")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("入錯commmand")   
        else:
            await ctx.send("輸入錯咗")    
        


def setup(bot):
    bot.add_cog(Main(bot))