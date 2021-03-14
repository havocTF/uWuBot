import discord
from discord.ext import commands
from pymongo import MongoClient

bot_channel = 810248103654588449
talk_channels = [810248103654588449]

cluster = MongoClient(
    'mongodb+srv://havoc:<Lucifer2020>@bot.pexmm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

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
            stats = levelling.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id, "rating": 100}
                    levelling.insert_one(newuser)
                else:
                    rating = stats["rating"] + 5
                    levelling.update_one({'id': message.author.id}, {'$set': rating})

    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.id == bot_channel:
            stats = levelling.find_one({"id": ctx.author.id})
            if stats is None:
                await ctx.channel.send('You have not had any interaction with her yet!')
            else:
                rating = stats['rating']
                await ctx.channel.send(rating)


def setup(client):
    client.add_cog(levelsys(client))
