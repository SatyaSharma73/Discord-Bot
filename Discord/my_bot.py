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
    
#Client (Our Bot)
client=discord.Client()

@client.event
async def on_ready():
    #Do Something--
    general_channel=client.get_channel(763964600969330698)
    await general_channel.send("How you guys doing !") #Sending Any Message

@client.event
async def on_message(Message):
  
    if Message.content=='what is the version' or Message.content=='WHAT IS THE VERSION' or Message.content=='What is the version':
        general_channel=client.get_channel(763964600969330698)

        myEmbed=discord.Embed(title="Current version",description="The bot is in version 1.0",color=0x00ff00)
        myEmbed.add_field(name="version Code:",value="v1.0.0",inline=True)
        myEmbed.add_field(name="Date Released :",value="july 10th,2020",inline=True)
        myEmbed.set_footer(text="Thank-you !! ")
        # myEmbed.set_author(name="Satya")
        await general_channel.send(embed=myEmbed)
    if Message.content=="Which master do you serve ?" or Message.content=="Which master do you serve ?" or Message.content=="WHICH MASTER DO YOU SERVE ?":
        general_channel=client.get_channel(763964600969330698)
        await general_channel.send("Am glad that you asked ,I was made to sever the MANKIND ")
    
    if Message.content=="what can you do for me ?" or Message.content=="What can you do for me ?" or Message.content=="WHAT CAN YOU DO FOR ME ?":
        general_channel=client.get_channel(763964600969330698)
        await general_channel.send("My ablities are getting better day by day , But now i am Under Development ")

    if Message.content=="How could you help me ?" or Message.content=="how could you help me ?" or Message.content=="HOW COULD YOU HELP ME ?":
        general_channel=client.get_channel(763964600969330698)
        await general_channel.send("These are the things i can let you know :")
        things=['For version Type - what is the version','For personal stuffs type - Which master do you serve ?']
        for i in things:
            await general_channel.send(i)

            
@client.event
async def on_disconnect():
    general_channel=client.get_channel(763964600969330698)
    await general_channel.send("GoodByeeeeeeee!") #Sending Any Message

#Put's the BOT ONLINE
client.run('NzYzOTYyODcxMzY0NzE0NTA3.X3_V3g.rY9bC_l-2j52NGcmifCCZ3kp-vQ') 




