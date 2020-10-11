import discord
from discord.ext import commands

#Client (Our Bot)
#client=discord.Client()
client=commands.Bot(command_prefix='==')

@client.command(name='version')
async def version(context):

    myEmbed=discord.Embed(title="Current version",description="The bot is in version 1.0",color=0x00ff00)
    myEmbed.add_field(name="version Code:",value="v1.0.0",inline=False)
    myEmbed.add_field(name="Date Released :",value="july 10th,2020",inline=False)
    myEmbed.set_footer(text="This is a sample Footer")
    myEmbed.set_author(name="Satya")
    
    await context.Message.send(embed=myEmbed)

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
            myEmbed.add_field(name="version Code:",value="v1.0.0",inline=False)
            myEmbed.add_field(name="Date Released :",value="july 10th,2020",inline=False)
            myEmbed.set_footer(text="This is a sample Footer")
            myEmbed.set_author(name="Satya")
            await general_channel.send(embed=myEmbed)

        await client.process_commands(Message)
            
# @client.event
# async def on_message_delete(Message):
#     author=Message.author
#     content=Message.content
#     channel=Message.general_channel
#     general_channel=client.get_channel(763964600969330698)
#     await general_channel.send(channel,'{}:{}'.format(author,content))

# @client.event
# async def on_disconnect():
#     general_channel=client.get_channel(763964600969330698)
#     await general_channel.send("GoodByeeeeeeee!") #Sending Any Message

#Put's the BOT ONLINE
client.run('NzYzOTYyODcxMzY0NzE0NTA3.X3_V3g.0g0HpT_j4L4eZ1cmKelrOMGE9lM') 





