from discord.ext import commands
from decouple import config
from discord import Intents


intents = Intents.all()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=intents)

    async def startup(self):
        await bot.wait_until_ready()
        await bot.tree.sync()
        print(f"Conectado em {bot.user}\nID: {bot.user.id}")

    async def setup_hook(self):
        await bot.load_extension("chat")
        await bot.load_extension("sync")
        await bot.load_extension("manager")
        self.loop.create_task(self.startup())



bot = Bot()
TOKEN = config('TOKEN')
bot.run(TOKEN)
