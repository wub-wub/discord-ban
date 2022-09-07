import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="your prefix here") # add a prefix for your bot, EG. "<" or "!" 

token = "your token here" #add your discord bots token here

#bot online -
@bot.event
async def on_ready():
    print ("the bot is ready!")

#ban command - 
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *,reason="Not defined"):
    await ctx.send(f"{member.mention} has been banned from {ctx.guild} by {ctx.author} for {reason}")
    await member.ban(reason=reason)
    
bot.run(token)
