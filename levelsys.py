import asyncio

import discord
from discord.ext import commands
from pymongo import MongoClient
import random

client = commands.Bot(command_prefix='~', intents=discord.Intents.all())

bot_channel = 810248103654588449
talk_channels = [810248103654588449]

cluster = MongoClient('mongodb+srv://havoc:Lucifer2020@bot.pexmm.mongodb.net/bot?retryWrites=true&w'
                      '=majority')

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
                    pass

    @commands.command(name='talk')
    async def talk(self, ctx):
        global shesays
        cases = random.randint(1, 7)
        if cases == 1:
            shesays = "*I really want to torture somebody :confounded:*"
            embed = discord.Embed(
                title="You let her talk about herself",
                description=shesays,
                colour=discord.Colour.dark_red()
            )
            embed.set_footer(text='*She likes you more. + 2 rating*')
            embed.set_image(
                url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
            stats = levelling.find_one({"id": ctx.author.id})
            rating = stats["rating"] + 2
            levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
            await ctx.channel.send(embed=embed)
        if cases == 2:
            shesays = "'*Pleasure is sweetest 'tis when paid for by another's pain -Ovid*'"
            embed = discord.Embed(
                title="You let her talk about herself",
                description=shesays,
                colour=discord.Colour.dark_red()
            )
            embed.set_footer(text='*She likes you more. + 2 rating*')
            embed.set_image(
                url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
            stats = levelling.find_one({"id": ctx.author.id})
            rating = stats["rating"] + 2
            levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
            await ctx.channel.send(embed=embed)
        if cases == 3:
            shesays = "*It's such a thrill, making another person plead for their life!*"
            embed = discord.Embed(
                title="You let her talk about herself",
                description=shesays,
                colour=discord.Colour.dark_red()
            )
            embed.set_footer(text='*She likes you more. + 2 rating*')
            embed.set_image(
                url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
            stats = levelling.find_one({"id": ctx.author.id})
            rating = stats["rating"] + 2
            levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
            await ctx.channel.send(embed=embed)
        if cases == 4:
            shesays = "*I want to shred you into pieces and hang you up on my wall~*"
            embed = discord.Embed(
                title="You let her talk about herself",
                description=shesays,
                colour=discord.Colour.dark_red()
            )
            embed.set_footer(text='*She likes you more. + 2 rating*')
            embed.set_image(
                url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
            stats = levelling.find_one({"id": ctx.author.id})
            rating = stats["rating"] + 2
            levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
            await ctx.channel.send(embed=embed)
        if cases == 5:
            shesays = "*How I relieve my stress is by messing up the insides of another person!*"
            embed = discord.Embed(
                title="You let her talk about herself",
                description=shesays,
                colour=discord.Colour.dark_red()
            )
            embed.set_footer(text='*She likes you more. + 2 rating*')
            embed.set_image(
                url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
            stats = levelling.find_one({"id": ctx.author.id})
            rating = stats["rating"] + 2
            levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
            await ctx.channel.send(embed=embed)
        if cases == 6:
            embed = discord.Embed(
                title="",
                description="***How do you like to relieve your stress?***",
                colour=discord.Colour.blue()
            )
            embed.add_field(name='Option A', value="I like to read books if I'm feeling stressed", inline=True)
            embed.add_field(name='Option B',
                            value="I like to inflict psychological stress on others for fun",
                            inline=True)
            embed.add_field(name='Option C',
                            value='I like to go outside and walk around my neighborhood to relieve stress',
                            inline=True)
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/810248103654588449/820868806145867796/yesss_2.jpg')
            embed.set_footer(text='Type either a, b, or c to answer')

            sent = await ctx.send(embed=embed)

            try:
                msg = await self.client.wait_for(
                    "message",
                    timeout=60,
                    check=lambda message: message.author == ctx.author
                                          and message.channel == ctx.channel
                )
                if msg:
                    await sent.delete()
                    await msg.delete()

                if msg.content == 'a':
                    embed = discord.Embed(
                        title="Oh..!",
                        description="*So you're just everyone else*",
                        colour=discord.Colour.dark_grey()
                    )
                    embed.set_image(url='https://cdn.discordapp.com/attachments/810248103654588449/820889609881780224/unknown.png')
                    embed.set_footer(text='Awww, you have lost 10 rating')
                    await ctx.send(embed=embed)
                    stats = levelling.find_one({"id": ctx.author.id})
                    rating = stats["rating"] - 10
                    levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
                if msg.content == 'b':
                    embed = discord.Embed(
                        title="Nice!",
                        description='*Wow, we may have more in common than I thought*',
                        colour=discord.Colour.dark_purple()
                    )
                    embed.set_image(url='https://cdn.discordapp.com/attachments/810248103654588449/820885814501965834/f9a353abbdfc5660eee84c9fe9a6e4c7.png')
                    embed.set_footer(text='Well done, you have gained 5 rating')
                    await ctx.send(embed=embed)
                    stats = levelling.find_one({"id": ctx.author.id})
                    rating = stats["rating"] + 5
                    levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
                if msg.content == 'c':
                    embed = discord.Embed(
                        title="Oh..!",
                        description="*So you're just everyone else*",
                        colour=discord.Colour.dark_grey()
                    )
                    embed.set_image(url='https://cdn.discordapp.com/attachments/810248103654588449/820889609881780224/unknown.png')
                    embed.set_footer(text='Awww, you have lost 10 rating')
                    await ctx.send(embed=embed)
                    stats = levelling.find_one({"id": ctx.author.id})
                    rating = stats["rating"] - 10
                    levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})

            except asyncio.TimeoutError:
                await sent.delete()
                await ctx.send("Cancelling due to timeout.", delete_after=10)
        if cases == 7:
            embed = discord.Embed(
                title="",
                description="***You ever feel like murdering someone?***",
                colour=discord.Colour.blue()
            )
            embed.add_field(name='Option A', value="I love killing other people in my spare time!", inline=True)
            embed.add_field(name='Option B',
                            value="Killing is wrong! I'm a law abiding citizen!",
                            inline=True)
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/810248103654588449/820868806145867796/yesss_2.jpg')
            embed.set_footer(text='Type either a or b')

            sent = await ctx.send(embed=embed)

            try:
                msg = await self.client.wait_for(
                    "message",
                    timeout=60,
                    check=lambda message: message.author == ctx.author
                                          and message.channel == ctx.channel
                )
                if msg:
                    await sent.delete()
                    await msg.delete()

                if msg.content == 'a':
                    embed = discord.Embed(
                        title="Nice!",
                        description="*I love murdering as well!*",
                        colour=discord.Colour.dark_purple()
                    )
                    embed.set_image(
                        url='https://cdn.discordapp.com/attachments/810248103654588449/820885814501965834/f9a353abbdfc5660eee84c9fe9a6e4c7.png')
                    embed.set_footer(text='You have gained 5 rating')
                    await ctx.send(embed=embed)
                    stats = levelling.find_one({"id": ctx.author.id})
                    rating = stats["rating"] + 5
                    levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
                if msg.content == 'b':
                    embed = discord.Embed(
                        title="You motherf*cker!",
                        description="*You boring little piss baby. I bet you can't do shit with your life*",
                        colour=discord.Colour.dark_grey()
                    )
                    embed.set_image(
                        url='https://cdn.discordapp.com/attachments/810248103654588449/820889609881780224/unknown.png')
                    embed.set_footer(text='You have lost 10 rating')
                    await ctx.send(embed=embed)
                    stats = levelling.find_one({"id": ctx.author.id})
                    rating = stats["rating"] - 10
                    levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})

            except asyncio.TimeoutError:
                await sent.delete()
                await ctx.send("Cancelling due to timeout.", delete_after=10)

        # REUSING CODE GO BRRRRRRRRRRRRRRRR

    @commands.command(name='rating')
    async def rating(self, ctx):
        if ctx.channel.id == bot_channel:
            stats = levelling.find_one({"id": ctx.author.id})
            if stats is None:
                await ctx.channel.send('You have not had any interaction with her yet!')
            else:
                rating = stats['rating']
                embed = discord.Embed(
                    title="Your rating",
                    description=rating,
                    colour=discord.Colour.dark_red()
                )
                await ctx.channel.send(embed=embed)

    @commands.command(name='godisdead')
    async def godisdead(self, ctx):
        embed = discord.Embed(
            title="She agrees with you",
            description='+5 rating',
            colour=discord.Colour.dark_red()
        )
        embed.set_image(
            url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
        stats = levelling.find_one({"id": ctx.author.id})
        rating = stats["rating"] + 5
        levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(levelsys(client))
