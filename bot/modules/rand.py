#---==IMPORTS==---
import random
from discord.ext import commands

#---==CONFIG==---
MAX_ROLLS = 10
MAX_DIE = 100

#---==COMMANDS==---
class rand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rand(self, ctx, end : int, begin : int = 0, size : int = 1):
        """Chooses a random number."""
        await ctx.send(random.randrange(begin, end, size))

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices : str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @commands.command()
    async def flip(self, ctx):
        """Flips a coin."""
        await ctx.send(random.choice(['Heads','Tails']))

    @commands.command()
    async def roll(self, ctx, dice : str = '1d100'):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        if 1 <= rolls <= MAX_ROLLS and 1 <= limit <= MAX_DIE:
            roll_results = []
            for r in range(rolls):
                roll_results.append(random.randint(1, limit))

            num_list = ', '.join(str(r) for r in roll_results)
            await ctx.send(f'{sum(roll_results)} = {num_list}')
        else:
            await ctx.send(f'The max number of dice that can be rolled is {MAX_ROLLS} and the max number of sides a die can have is {MAX_DIE}.')

async def setup(bot):
    await bot.add_cog(rand(bot))