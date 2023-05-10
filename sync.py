import discord
from discord.ext import commands



class Sync(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def sync(self, ctx) -> None:
        id = 1043512790217932821
        if ctx.author.id == 1043512790217932821:
            fnt = await ctx.bot.tree.sync()
            await ctx.send(f'synced {len(fnt)} commands.')
        else:
            ctx.send("So o dono deste bot pode usar este comando")
        


async def setup(bot):
    await bot.add_cog(Sync(bot))