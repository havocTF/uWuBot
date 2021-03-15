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
        cases = random.randint(6, 6)
        if cases == 1:
            shesays = "*I really want to torture somebody :confounded:*"
        if cases == 2:
            shesays = "'*Pleasure is sweetest 'tis when paid for by another's pain -Ovid*'"
        if cases == 3:
            shesays = "*It's such a thrill, making another person plead for their life!*"
        if cases == 4:
            shesays = "*I want to shred you into pieces and hang you up on my wall~*"
        if cases == 5:
            shesays = "*How I relieve my stress is by messing up the insides of another person!*"
        if cases == 6:
            embed = discord.Embed(
                titles="Question",
                description="*How do you like to relive your stress?*",
                colour=discord.Colour.blue()
            )
            embed.add_field(name='Option A', value="I like to read books if I'm feeling stressed", inline=True)
            embed.add_field(name='Option B',
                            value="I like to let someone inflict pain or humiliation on me if I'm feeling stressed",
                            inline=True)
            embed.add_field(name='Option C',
                            value='I like to go outside and walk around my neighborhood to relieve my stress',
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
                if msg.content == 'b':
                    embed = discord.Embed(
                        title="Nice!",
                        description='*Wow, we may have more in common than I thought*',
                        colour=discord.Colour.dark_purple()
                    )
                    embed.set_image(url='https://cdn.discordapp.com/attachments/810248103654588449/820885814501965834/f9a353abbdfc5660eee84c9fe9a6e4c7.png')
                    embed.set_footer(text='Well done, you have gained 5 rating')
                    await ctx.send(embed=embed)
                if msg.content == 'c':
                    embed = discord.Embed(
                        title="Oh..!",
                        description="*So you're just everyone else*",
                        colour=discord.Colour.dark_grey()
                    )
                    embed.set_image(url='https://cdn.discordapp.com/attachments/810248103654588449/820889609881780224/unknown.png')
                    embed.set_footer(text='Awww, you have lost 10 rating')
                    await ctx.send(embed=embed)

            except asyncio.TimeoutError:
                await sent.delete()
                await ctx.send("Cancelling due to timeout.", delete_after=10)

        #embed = discord.Embed(
        #    title="You let her talk about herself",
        #    description=shesays,
        #    colour=discord.Colour.dark_red()
        #)
        #embed.set_footer(text='*She likes you more. + 5 rating*')
        #embed.set_image(
        #    url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
        # embed.set_thumbnail(
        # url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
        # embed.set_author(name='She says',
        # icon_url='https://cdn.discordapp.com/avatars/820083661982007317/a3b247b4f68918b9591668ae52ce910e.webp?size=128')
        # embed.add_field(name='Rating', value='*she likes you more* "`yaml +5 rating', inline=False)
        # embed.add_field(name='Field Name', value='Field Value', inline=True)
        # embed.add_field(name='Field Name', value='Field Value', inline=True)
        #stats = levelling.find_one({"id": ctx.author.id})
        #rating = stats["rating"] + 5
        #levelling.update_one({'id': ctx.author.id}, {'$set': {'rating': rating}})
        #await ctx.channel.send(embed=embed)

        #embed = discord.Embed(
        #   title="please tell me what you want me to repeat",
        #    description="this will timeout after 1 minute"

        #)
        #sent = await ctx.send(embed=embed)

        #try:
        #    msg = await self.client.wait_for(
        #        "message",
        #        timeout=60,
        #        check=lambda message: message.author == ctx.author
        #                              and message.channel == ctx.channel
        #    )
        #    if msg:
        #        await sent.delete()
        #        await msg.delete()
        #        await ctx.send(msg.content)

        #except asyncio.TimeoutError:
        #    await sent.delete()
        #    await ctx.send("Cancelling due to timeout.", delete_after=10)

    @commands.command(name="echo")
    async def echo(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title="please tell me what you want me to repeat",
            description="this will timeout after 1 minute"

        )
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
                await ctx.send(msg.content)

        except asyncio.TimeoutError:
            await sent.delete()
            await ctx.send("Cancelling due to timeout.", delete_after=10)

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
