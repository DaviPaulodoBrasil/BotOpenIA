from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument
from discord.ext import commands



class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('ok')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.reply('Comando não encontrado use \"!help\"')
        elif isinstance(error, MissingRequiredArgument):
            await ctx.reply('Você não passou todos os comandos!')
        else:
            await ctx.reply(f'Erro na execução do comado \n nome do erro -> {error}')



async def setup(bot):
    await bot.add_cog(Manager(bot))