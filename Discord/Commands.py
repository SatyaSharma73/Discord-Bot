import discord
from discord.ext import commands
import random


client = commands.Bot(command_prefix=".")
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

@client.command()
async def version(ctx):

    myEmbed=discord.Embed(title="Current version",description="The bot is in version 1.0",color=discord.Color.blue())
    myEmbed.add_field(name="Version Code:",value="v1.0.0",inline=True)
    myEmbed.add_field(name="Date Released :",value="july 10th,2020",inline=True)
    myEmbed.set_footer(text="Thank-you !! ")

    await ctx.send(embed=myEmbed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping - {round(client.latency*1000)} ms')


@client.command(aliases=['8ball','test'])
async def _8ball(ctx,*,question):
    responses = ['It is certain','It is decidedly so.','Yes - definitely','without a doubt','As I see it , yes',
                'Most likely','Outlook good','Yes','Signs point to yes','Reply hazy, try again','Better not tell you now',
                'Concentrate and ask again','Very doubtful.','outlook not so good',"Don't count on me",'Cannot predict right now']
    await ctx.send(f'Question :{question}\nAnswer :{random.choice(responses)}')


@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def ban(ctx,member:discord.Member,*,reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx,*,member):
    banned_user= await ctx.guild.bans()
    member_name,member_discriminator=member.split('#')

    for ban_entry in banned_user:
        user=ban_entry.user

        if (user.name,user.discriminator)==(member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
        
        
        
@client.command()
async def helpme(context):

    myEmbed=discord.Embed(title="Here are some Commands i can do for you just type Below mentioned  ",
                          description="1) .Server\n2) .version\n3) .ping\n4) .8ball\n5) .clear\n6.) .kick\n7) .ban\n8) .unban",
                          color=discord.Color.red())
    myEmbed.add_field(name="v0.1 Commands ",value="12th Oct,2020",inline=True)
    myEmbed.set_footer(text="Thank-you !! ")

    await context.send(embed=myEmbed)



client.run('NzYzOTYyODcxMzY0NzE0NTA3.X3_V3g.LoFdpPxgCcV-Mn9zg6rw-bxEerA') 
