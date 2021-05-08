import discord
import asyncio
import random
import requests
import googletrans
from googletrans import Translator
import os

TOKEN = os.environ.get('BOT_TOKEN')

maps = ["dust", "nuke", "mirage", "mocha", "inferno"]

class Disociate(discord.Client):

    async def on_ready(self):
        print(f'{self.user} подключён к Discord')
        for guild in client.guilds:
            print(
                f'{client.user} подключился к каналу:\n'
                f'{guild.name} (id: {guild.id})'
            )

    async def on_message(self, message):
         if message.content.startswith("!максим"):
            count = int(message.content.split()[1])
            while count != 0:
                await message.channel.send("@Максим")
                count = count - 1
                await asyncio.sleep(5)
        if message.content.startswith("!помощь"):
            await message.channel.send('''Список команд:
             !орел и решка - по названию не понятно?
             !таймер (кол-во часов) часов (кол-во минут) минут - ну таймер типа...
             !мкс - выводит текущее положение мкс (зачем?...)
             !карта - выводит рандомную карту (вдруг не можете определиться)
             !максим (кол-во раз) - зовет максима определенное количество раз''')
        if message.content.startswith("!мкс"):
            res = requests.get("http://api.open-notify.org/iss-now.json")
            obj = res.json()
            await message.channel.send(f"{obj['iss_position']['latitude']}")
            await message.channel.send(f"{obj['iss_position']['longitude']}")
        if message.content.startswith("!таймер"):
            hours, minutes = int(message.content.split()[1]), int(message.content.split()[3])
            await message.channel.send(f':gosling: Таймер сработает через {hours} hours и {minutes} minutes')
            await asyncio.sleep(hours * 3600 + minutes * 60)
            await message.channel.send(
                "Ну как там с часами :dengi:")
        if message.content.startswith("!орел и решка"):
            answer = random.randint(1, 2)
            if answer == 1:
                answer = 'Орёл!'
            else:
                answer = "Решка!"
            await message.channel.send("Ща подкину")
            await asyncio.sleep(3)
            await message.channel.send("Блин, укатилась, ща подниму")
            await asyncio.sleep(5)
            await message.channel.send(f"{answer}")
        if message.content.startswith("!карта"):
            mapa = random.randint(0, 4)
            ans = maps[mapa]
            await message.channel.send(f"{ans}")
        if message.content.startswith('!переводчик'):
            needtrans = message.content[12:]
            translator = Translator()
            result = translator.translate(needtrans, dest='ru').text
            await message.channel.send(result)


client = Disociate()
client.run(TOKEN)
