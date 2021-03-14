import discord
from discord.ext import commands
from pymongo import MongoClient

bot_channel = 810248103654588449
talk_channels = [810248103654588449]

cluster = MongoClient('mongodb+srv://havoc:<Lucifer2020>@bot.pexmm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

levelling = cluster['discord']['levelling']

class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('ready!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = levelling.find_one({"id":})