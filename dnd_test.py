import discord

# client = discord.Client()
from discord.ext import commands
bot = commands.Bot(command_prefix='$')
    
@bot.command()
async def addChar(ctx, *args):
	print('Got something')
	await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


bot.run('Njc3Mjc2MTQ5MTQ3MTA3MzI5.XkR57w.u_oThucdrIPWRLWxACgc7dpDrM4')
