import discord
from discord.ext import commands 


bad_words = ["abe","salle","kutte"]


cleint = commands.Bot(command_prefix=">")




@cleint.event
async def on_message(message):
    message.content = message.content.lower()
    for word in bad_words:
        if message.content.count(word) >0:
            await message.channel.purge(limit=1)

    await cleint.process_commands(message)


@cleint.event
async def on_message(message):
    message.content = message.content.lower()

    if message==('hello', ctx  ):
        await ctx.send("hi")
    

@cleint.command
async def members(ctx):

        embed = discord.Embed(title=f"There are {len(ctx.guild.members)} members in {ctx.guild.name}!", colour=0xffff00, timestamp=ctx.message.created_at)
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)

        await ctx.send(embed=embed)   

@cleint.event
async def on_message(message):
    message.content = message.content.lower()
    for word in bad_words:
        if message.content.count(word) >0:
            await message.channel.purge(limit=1)

    await cleint.process_commands(message)


@cleint.command()
async def hello(ctx):
    if str(ctx.author) == '𝐀尺𝐂 × 𝐅ΔҠΞ〢 BEASTᴿᵃʷ#6999':
        await ctx.send(f"Hello {ctx.author}")


@cleint.command()
async def youtube(url):
    await url.send("https://www.youtube.com/channel/UCD7yrMxncusG7aEINZiE2RA")


@cleint.command()
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url

    embed = discord.Embed(colour=member.color , timestamp=ctx.message.created_at)
    embed.set_author(name=f"Author of {member}")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)





cleint.run("ODE4MTYxMjY4Mjg3NzMzNzkw.YEUCDw.DF5-_5VMnVzYXhbWwqygfUgp8qY")
