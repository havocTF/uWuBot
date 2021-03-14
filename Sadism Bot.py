import discord
from discord.ext import commands
import random
import levelsys

cogs = [levelsys]

client = commands.Bot(command_prefix='~', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


@client.command(name='version')
async def version(context):
    await context.message.channel.send('Version 1.0')


@client.command(name='uwu')
async def uwu(context):
    await context.message.channel.send('*unzips your pants*')


@client.command(name='m')
async def m(context):
    await context.message.channel.send("I'm going to slap you and you're going to like it")


@client.command(name='why')
async def why(context):
    await context.message.channel.send("I was created to fulfill your masochistic desires :>")


@client.command(name='masochism')
async def what(context):
    await context.message.channel.send("Masochism is when you get pleasure from being in pain or being humiliated")


@client.command(name='kaedebad')
async def KaedeBad(context):
    await context.message.channel.send("*listen here you little shit I will fucking kill you*")


@client.command(name='waifu')
async def Kaede(context):
    await context.message.channel.send("kaede is bestest wafii")


@client.command(name='cult')
async def cult(context):
    await context.message.channel.send("***JOIN THE KAEDE CULT NOW***")


@client.command(name='ara')
async def ara(context):
    await context.message.channel.send("*ara ara onii-chan*")


@client.command(name='china')
async def china(context):
    await context.message.channel.send("*message retracted*")


@client.command(name='bestanime')
async def bestanime(context):
    await context.message.channel.send('The best anime of all time is objectively phineas and furb')


@client.command(name='ramen')
async def ramen(context):
    await context.message.channel.send("Here is your ramen good sir :ramen:")


@client.command(name='food')
async def food(context):
    global realtextfoodtext
    randomFood = random.randint(0, 61)
    foods = [':grapes:', ':melon:', ':watermelon:', ':tangerine:', ':lemon:', ':banana:', ':pineapple:', ':mango:',
             ':apple:', ':green_apple:', ':pear:', ':peach:', ':cherries:', ':strawberry:', ':coconut:', ':avocado:',
             ':eggplant: hehe', ':potato:', ':carrot:', ':ear_of_corn:', ':hot_pepper:', ':cucumber:', ':leafy_green:',
             ':broccoli:', ':garlic:', ':onion:', ':mushroom:', ':peanuts:', ':chestnut:', ':bread:', ':croissant:',
             ':french_bread:', ':pretzel:', ':bagel:', ':pancakes:', ':waffle:', ':cheese:', ':meat_on_bone:',
             ':bacon:', ':hamburger:', ':fries:', ':pizza:', ':hotdog:', ':sandwich:', ':taco:', 'burrito:',
             ':stuffed_flatbread:', ':falafel:', ':egg:', ':bowl_with_spoon:', ':salad:', ':popcorn:', ':bento:',
             ':rice_cracker:', ':rice_ball:', ':rice:', ':spaghetti:', ':sushi:', ':fried_shrimp:', ':takeout_box:',
             ':fortune_cookie:', ':cup_with_straw:']
    textfood = foods[randomFood]
    textfoodtext = textfood[1:-1]
    findunderscore = '_'
    if findunderscore in textfoodtext:
        realtextfoodtext = textfoodtext.replace('_', ' ')
        await context.message.channel.send("Here is your " + realtextfoodtext + " good sir " + textfood)
    else:
        await context.message.channel.send("Here is your " + textfoodtext + " good sir " + textfood)


@client.command(name='sadism')
async def sadism(context):
    cases = random.randint(1, 5)
    if cases == 1:
        await context.message.channel.send("I really want to torture somebody :confounded:")
    if cases == 2:
        await context.message.channel.send("*Pleasure is sweetest 'tis when paid for by another's pain* -Ovid")
    if cases == 3:
        await context.message.channel.send("It's such a thrill, making another person plead for their life!")
    if cases == 4:
        await context.message.channel.send("I want to shred you into pieces and hang you up on my wall~")
    if cases == 5:
        await context.message.channel.send("How I relieve my stress is by messing up the insides of another person!")


@client.command(name='top10waifus')
async def top10waifus(context):
    await context.message.channel.send(
        "1. Kaede\n2. Kaede\n3. Kaede\n4. Kaede\n5. Kaede\n6. Speedwagon\n7. Kaede\n8. Kaede\n9. Kaede\n10. Kaede")


@client.command(name='ppsize')
async def ppsize(context):
    a = random.randint(1, 10)
    pp = str(a)
    if a == 1:
        await context.message.channel.send('oh fuck. yikes man u got a 1 incher')
    else:
        await context.message.channel.send(pp + ' inches')
        if a >= 6:
            await context.message.channel.send("Wow! That's a big pp! Girls must be frothing over your dick")
        if a <= 5:
            await context.message.channel.send("Wow! That's a pretty nice micro penis you have there!")


@client.command(name='doyouloveme')
async def doyouloveme(context):
    await context.message.channel.send("of course, darling :blush:")


@client.command(name='sex?')
async def sex(context):
    await context.message.channel.send("aww, yes darling :kissing_closed_eyes:")


@client.command(name='dev')
async def dev(context):
    await context.message.channel.send("havoc chan made me <3")


@client.command(name='hug')
async def hug(context):
    user = context.message.author.name
    await context.message.channel.send("I love you, " + user)


@client.command(name='holdhands')
async def holdhands(context):
    username = context.message.author.name
    await context.message.channel.send("your hands are warm, " + username + " :blush:")


@client.command(name='killme')
async def killme(context):
    username = context.message.author.name
    await context.message.channel.send(
        "oh " + username + ", but we just started having fun :smiling_face_with_3_hearts:")


@client.event
async def on_error(context):
    if on_error():
        await context.message.channel.send("**You dumb piece of shit that's not a command**")


@client.event
async def on_ready():
    general_channel = client.get_channel(810248103654588449)
    await general_channel.send('@everyone fuck me in the pussi')
    await client.change_presence(status=discord.Status.do_not_disturb,
                                 activity=discord.Game('Masochizing Mllions of Children Around the World'))


@client.event
async def on_message(message):
    if message.content == 'pi':
        general_channel = client.get_channel(810248103654588449)
        await general_channel.send(
            '3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 '
            '3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 '
            '6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 '
            '4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540 9171536436 7892590360 '
            '0113305305 4882046652 1384146951 9415116094 3305727036 5759591953 0921861173 8193261179 3105118548 '
            '0744623799 6274956735 1885752724 8912279381 8301194912 9833673362 4406566430 8602139494 6395224737 '
            '1907021798 6094370277 0539217176 2931767523 8467481846 7669405132 0005681271 4526356082 7785771342 '
            '7577896091 7363717872 1468440901 2249534301 4654958537 1050792279 6892589235 4201995611 2129021960 '
            '8640344181 5981362977 4771309960 5187072113 4999999837 2978049951 0597317328 1609631859 5024459455 '
            '3469083026 4252230825 3344685035 2619311881 7101000313 7838752886 5875332083 8142061717 7669147303 '
            '5982534904 2875546873 1159562863 8823537875 9375195778 1857780532 1712268066 1300192787 6611195909 '
            '2164201989')
    if message.content == '(.)(.)':
        general_channel = client.get_channel(810248103654588449)
        await general_channel.send('PLEASE OPPAI MAKE ME HORNI')
    await client.process_commands(message)


client.run('ODIwMDgzNjYxOTgyMDA3MzE3.YEwAbQ.nQHPh1nPZ9WaI-AIMeeTbpqW5go')
