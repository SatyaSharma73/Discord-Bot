import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")
@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


client= commands.Bot(command_prefix = "~")
@client.command()
async def version(ctx):

    myEmbed=discord.Embed(title="Current version",description="The bot is in version 1.0",color=discord.Color.blue())
    myEmbed.add_field(name="Version Code:",value="v1.0.0",inline=True)
    myEmbed.add_field(name="Date Released :",value="july 10th,2020",inline=True)
    myEmbed.set_footer(text="Thank-you !! ")

    await ctx.send(embed=myEmbed)

client.run('NzYzOTYyODcxMzY0NzE0NTA3.X3_V3g.rY9bC_l-2j52NGcmifCCZ3kp-vQ') 
