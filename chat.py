from discord.ext import commands
from discord import app_commands
from discord import Interaction
from senha import API_KEY
import requests
import json


class Chat(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot =  bot


    @app_commands.command(name="chat", description="Devolve a resposta da IA CHAT GPT 3.5")
    async def chat(self, interaction: Interaction,  pergunta: str):
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        link = "https://api.openai.com/v1/chat/completions"
        id_modelo = "gpt-3.5-turbo"

        pergunta = str(pergunta)

        body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": pergunta}]
        }
        body_mensagem = json.dumps(body_mensagem)
        requisicao = requests.post(link, headers=headers, data=body_mensagem)
        
        resposta = requisicao.json()
        mensagem = resposta["choices"][0]["message"]["content"]

        await interaction.response.send_message(mensagem)




async def setup(bot):
    await bot.add_cog(Chat(bot))
